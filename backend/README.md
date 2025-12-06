# ⚙️ Backend - سرور و API

این پوشه شامل کد Backend و API های پروژه است.

---

## 🏗️ ساختار
```
backend/
├── api/                      ← API Routes
│   ├── kpis.py
│   ├── companies.py
│   ├── benchmarks.py
│   └── reports.py
│
├── models/                   ← Database Models
│   ├── kpi.py
│   ├── company.py
│   └── data_entry.py
│
├── validators/               ← Validation Engine
│   ├── smart_validator.py
│   ├── radar_validator.py
│   └── schema_validator.py
│
├── services/                 ← Business Logic
│   ├── kpi_service.py
│   ├── benchmark_service.py
│   └── report_service.py
│
├── utils/                    ← Utilities
│   ├── database.py
│   └── helpers.py
│
├── tests/                    ← Unit Tests
│
├── main.py                   ← Entry Point
├── requirements.txt          ← Dependencies
└── config.py                 ← Configuration
```

---

## 🚀 Technology Stack

### Framework
- **FastAPI** (Python) - توصیه می‌شود ✅
- یا **Express.js** (Node.js)

### Database
- **PostgreSQL 14+** - اصلی
- **Redis** - Cache

### ORM
- **SQLAlchemy** (Python)
- یا **Prisma** (Node.js)

---

## 📋 API Endpoints (برنامه‌ریزی شده)

### KPIs
```
GET    /api/v1/kpis              # لیست شاخص‌ها
GET    /api/v1/kpis/{code}       # جزئیات شاخص
POST   /api/v1/kpis              # ایجاد شاخص جدید
PUT    /api/v1/kpis/{code}       # به‌روزرسانی
DELETE /api/v1/kpis/{code}       # حذف
```

### Companies
```
GET    /api/v1/companies         # لیست شرکت‌ها
GET    /api/v1/companies/{id}    # جزئیات شرکت
POST   /api/v1/companies         # ثبت شرکت
```

### Data Entries
```
POST   /api/v1/data              # ثبت داده جدید
GET    /api/v1/data/{kpi_code}   # داده‌های یک شاخص
```

### Benchmarks
```
GET    /api/v1/benchmarks/{kpi_code}  # بنچمارک‌ها
```

### Reports
```
POST   /api/v1/reports/generate       # تولید گزارش
```

---

## 🔧 نصب و اجرا (آینده)
```bash
# نصب وابستگی‌ها
cd backend
pip install -r requirements.txt

# تنظیم متغیرهای محیطی
cp .env.example .env

# اجرای Migration
alembic upgrade head

# اجرای سرور
uvicorn main:app --reload
```

---

## 🧪 تست
```bash
# اجرای تست‌ها
pytest tests/

# Coverage
pytest --cov=backend tests/
```

---

## 🎯 نقشه راه

### Q2 2025
- [ ] راه‌اندازی FastAPI
- [ ] CRUD شاخص‌ها
- [ ] اعتبارسنجی SMART/RADAR
- [ ] API Documentation (Swagger)

### Q3 2025
- [ ] سیستم احراز هویت
- [ ] مدیریت شرکت‌ها
- [ ] ثبت داده و بنچمارک
- [ ] تولید گزارش

---

**نسخه:** 0.1.0  
**وضعیت:** برنامه‌ریزی شده  
**تاریخ:** 2025-01-15
