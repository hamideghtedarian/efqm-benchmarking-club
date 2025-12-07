# 🗄️ Database - پایگاه داده

این پوشه شامل Schema، Migrations و Seeds پایگاه داده است.

---

## 🏗️ ساختار
```
database/
├── migrations/              ← تغییرات Schema
│   ├── 001_initial_schema.sql
│   ├── 002_add_kpis_table.sql
│   ├── 003_add_companies_table.sql
│   └── ...
│
├── seeds/                   ← داده‌های اولیه
│   ├── kpis_seed.sql
│   ├── benchmarks_seed.sql
│   └── sample_data.sql
│
├── schema.sql               ← Schema کامل
├── indexes.sql              ← Indexes
├── views.sql                ← Views
└── functions.sql            ← Stored Functions
```

---

## 🗃️ Database Engine

**انتخاب اول:** PostgreSQL 14+

**چرا PostgreSQL؟**
- ✅ JSON Support (JSONB)
- ✅ Full-Text Search
- ✅ Performance بالا
- ✅ Open Source
- ✅ پشتیبانی از RTL

---

## 📊 جداول اصلی

### 1. kpis (شاخص‌ها)
```sql
CREATE TABLE kpis (
    id SERIAL PRIMARY KEY,
    kpi_code VARCHAR(20) UNIQUE NOT NULL,
    kpi_name_fa VARCHAR(255) NOT NULL,
    kpi_name_en VARCHAR(255) NOT NULL,
    criterion INTEGER NOT NULL CHECK (criterion IN (6, 7)),
    sub_criterion INTEGER NOT NULL,
    category VARCHAR(100),
    
    -- محتوای کامل JSON
    content JSONB NOT NULL,
    
    -- امتیازها
    smart_score INTEGER CHECK (smart_score >= 0 AND smart_score <= 100),
    radar_score INTEGER CHECK (radar_score >= 0 AND radar_score <= 100),
    
    -- وضعیت
    status VARCHAR(20) DEFAULT 'active',
    version VARCHAR(20) DEFAULT '1.0.0',
    
    -- تاریخ‌ها
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Indexes
    CONSTRAINT kpi_code_format CHECK (kpi_code ~ '^R[6-7]-[1-5]-[0-9]{3}$')
);

CREATE INDEX idx_kpis_code ON kpis(kpi_code);
CREATE INDEX idx_kpis_criterion ON kpis(criterion, sub_criterion);
CREATE INDEX idx_kpis_smart ON kpis(smart_score);
CREATE INDEX idx_kpis_content ON kpis USING GIN(content);
```

---

### 2. companies (شرکت‌ها)
```sql
CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    company_id VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    name_en VARCHAR(255),
    
    -- اطلاعات پایه
    industry VARCHAR(100),
    sub_industry VARCHAR(100),
    size VARCHAR(20) CHECK (size IN ('Small', 'Medium', 'Large')),
    employees INTEGER,
    revenue_million_usd DECIMAL(12, 2),
    
    -- مکان
    country VARCHAR(100),
    city VARCHAR(100),
    
    -- EFQM
    efqm_recognition VARCHAR(100),
    recognition_year INTEGER,
    
    -- تماس
    contact JSONB,
    
    -- تاریخ‌ها
    founded_year INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_companies_country ON companies(country);
CREATE INDEX idx_companies_industry ON companies(industry);
CREATE INDEX idx_companies_size ON companies(size);
```

---

### 3. data_entries (داده‌های واقعی)
```sql
CREATE TABLE data_entries (
    id SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES companies(id),
    kpi_code VARCHAR(20) REFERENCES kpis(kpi_code),
    
    -- دوره زمانی
    period VARCHAR(10) NOT NULL,  -- 2024-Q4 or 2024-12
    period_type VARCHAR(10) CHECK (period_type IN ('monthly', 'quarterly', 'yearly')),
    
    -- مقدار
    value DECIMAL(12, 4) NOT NULL,
    unit VARCHAR(50),
    
    -- منبع
    source VARCHAR(255),
    source_type VARCHAR(50),
    sample_size INTEGER,
    
    -- اعتبار
    verified BOOLEAN DEFAULT FALSE,
    verified_by INTEGER,
    verified_at TIMESTAMP,
    
    -- یادداشت‌ها
    notes TEXT,
    
    -- تاریخ‌ها
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Unique constraint
    UNIQUE(company_id, kpi_code, period)
);

CREATE INDEX idx_data_company ON data_entries(company_id);
CREATE INDEX idx_data_kpi ON data_entries(kpi_code);
CREATE INDEX idx_data_period ON data_entries(period);
```

---

### 4. benchmarks (بنچمارک‌ها)
```sql
CREATE TABLE benchmarks (
    id SERIAL PRIMARY KEY,
    kpi_code VARCHAR(20) REFERENCES kpis(kpi_code),
    
    -- نوع بنچمارک
    benchmark_type VARCHAR(50) NOT NULL,
    -- 'european_top_quartile', 'european_median', 
    -- 'industry_average', 'world_class'
    
    -- مقادیر
    value DECIMAL(12, 4) NOT NULL,
    
    -- جزئیات
    source VARCHAR(255),
    sample_size INTEGER,
    data_year INTEGER NOT NULL,
    
    -- فیلترها
    industry VARCHAR(100),
    country VARCHAR(100),
    company_size VARCHAR(20),
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    UNIQUE(kpi_code, benchmark_type, data_year, industry, country)
);

CREATE INDEX idx_benchmarks_kpi ON benchmarks(kpi_code);
CREATE INDEX idx_benchmarks_type ON benchmarks(benchmark_type);
CREATE INDEX idx_benchmarks_year ON benchmarks(data_year);
```

---

### 5. users (کاربران)
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    
    -- اطلاعات
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    company_id INTEGER REFERENCES companies(id),
    
    -- نقش
    role VARCHAR(20) DEFAULT 'user',
    -- 'admin', 'manager', 'user', 'viewer'
    
    -- وضعیت
    is_active BOOLEAN DEFAULT TRUE,
    email_verified BOOLEAN DEFAULT FALSE,
    
    -- تاریخ‌ها
    last_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_company ON users(company_id);
```

---

## 📈 Views

### view_kpi_summary
```sql
CREATE VIEW view_kpi_summary AS
SELECT 
    k.kpi_code,
    k.kpi_name_fa,
    k.kpi_name_en,
    k.criterion,
    k.sub_criterion,
    k.smart_score,
    k.radar_score,
    COUNT(de.id) as data_count,
    AVG(de.value) as avg_value
FROM kpis k
LEFT JOIN data_entries de ON k.kpi_code = de.kpi_code
GROUP BY k.id, k.kpi_code;
```

---

## 🔧 نصب و راه‌اندازی

### مرحله 1: نصب PostgreSQL
```bash
# Ubuntu/Debian
sudo apt install postgresql-14

# macOS
brew install postgresql@14

# Docker
docker run -d \
  --name efqm-postgres \
  -e POSTGRES_PASSWORD=yourpassword \
  -e POSTGRES_DB=efqm_club \
  -p 5432:5432 \
  postgres:14
```

---

### مرحله 2: ایجاد Database
```bash
# اتصال به PostgreSQL
psql -U postgres

# ایجاد Database
CREATE DATABASE efqm_club;

# ایجاد User
CREATE USER efqm_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE efqm_club TO efqm_user;
```

---

### مرحله 3: اجرای Schema
```bash
# اجرای Schema اصلی
psql -U efqm_user -d efqm_club -f database/schema.sql

# اجرای Indexes
psql -U efqm_user -d efqm_club -f database/indexes.sql

# اجرای Views
psql -U efqm_user -d efqm_club -f database/views.sql
```

---

### مرحله 4: Seed Data
```bash
# داده‌های اولیه
psql -U efqm_user -d efqm_club -f database/seeds/kpis_seed.sql
psql -U efqm_user -d efqm_club -f database/seeds/benchmarks_seed.sql
```

---

## 🔄 Migrations

استفاده از **Alembic** (Python) یا **Prisma Migrate** (Node.js)
```bash
# ایجاد Migration جدید
alembic revision -m "add_new_table"

# اعمال Migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

---

## 💾 Backup & Restore

### Backup
```bash
# Full Backup
pg_dump -U efqm_user efqm_club > backup_$(date +%Y%m%d).sql

# Schema Only
pg_dump -U efqm_user --schema-only efqm_club > schema_backup.sql

# Data Only
pg_dump -U efqm_user --data-only efqm_club > data_backup.sql
```

### Restore
```bash
psql -U efqm_user efqm_club < backup_20250115.sql
```

---

## 🎯 نقشه راه

### Q2 2025
- [ ] طراحی Schema کامل
- [ ] ایجاد جداول اصلی
- [ ] Indexes و Constraints
- [ ] Migration System

### Q3 2025
- [ ] Views و Functions
- [ ] Backup Strategy
- [ ] Performance Tuning
- [ ] Security Hardening

---

## 📊 حجم داده تخمینی

| جدول | تعداد ردیف | حجم |
|------|------------|-----|
| kpis | 90 | ~5 MB |
| companies | 1,000 | ~2 MB |
| data_entries | 100,000 | ~20 MB |
| benchmarks | 5,000 | ~1 MB |
| users | 500 | ~1 MB |

**جمع:** ~30 MB (سال اول)

---

**نسخه:** 0.1.0  
**وضعیت:** برنامه‌ریزی شده  
**تاریخ:** 2025-01-15
