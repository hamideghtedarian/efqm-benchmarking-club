# 🛠️ Tools - ابزارهای کمکی

این پوشه شامل ابزارهای CLI و اسکریپت‌های کمکی برای کار با پروژه است.

---

## 📊 وضعیت فعلی

**ابزار اصلی:** `kpi_generator.py` در Root پروژه قرار دارد

**ابزارهای این پوشه:** در حال توسعه 🔨

---

## 🔮 ابزارهای برنامه‌ریزی شده

### 1. kpi-validator-cli.py
**اعتبارسنجی شاخص‌ها**

```bash
python tools/kpi-validator-cli.py --file R6-1-003.json

# خروجی:
# ✅ SMART Score: 95/100 (Pass)
# ✅ RADAR Score: 90/100 (Pass)
# ✅ All validations passed!
```

**ویژگی‌ها:**
- بررسی کامل SMART (≥80)
- بررسی کامل RADAR (≥60)
- اعتبارسنجی JSON Schema
- تشخیص فیلدهای خالی
- پیشنهاد بهبود

---

### 2. batch-generator.py
**تولید دسته‌ای شاخص‌ها**

```bash
python tools/batch-generator.py --input kpis_batch_6-1.json

# خروجی:
# ⏳ Generating R6-1-005...
# ✅ Created: R6-1-005-product-quality-satisfaction.json
# ⏳ Generating R6-1-006...
# ✅ Created: R6-1-006-customer-satisfaction-score.json
# ...
# 🎉 Generated 11 KPIs successfully!
```

---

### 3. search-kpis.py
**جستجوی شاخص‌ها**

```bash
# جستجو با کلمه کلیدی
python tools/search-kpis.py --keyword "رضایت"

# جستجو با کد
python tools/search-kpis.py --code "R6-1-*"

# جستجو در دسته
python tools/search-kpis.py --category "customer"

# خروجی:
# Found 5 KPIs:
# - R6-1-001: رضایت کلی مشتریان
# - R6-1-006: رضایت از کیفیت محصول
# ...
```

---

### 4. benchmark-analyzer.py
**تحلیل بنچمارک‌ها**

```bash
python tools/benchmark-analyzer.py --kpi R6-1-001

# خروجی:
# 📊 Benchmark Analysis for R6-1-001
# 
# European Best Practice:
# - Top Quartile: 90%
# - Median: 75%
# - Bottom Quartile: 60%
# 
# Your Position: 82% (Above Median)
# Gap to Top Quartile: 8%
```

---

### 5. data-quality-checker.py
**بررسی کیفیت داده‌ها**

```bash
python tools/data-quality-checker.py --file data-entry.json

# بررسی:
# - Missing values
# - Outliers
# - Duplicates
# - Data types
# - Value ranges
```

---

### 6. import-benchmarks.py
**ایمپورت بنچمارک‌ها**

```bash
# از CSV
python tools/import-benchmarks.py --source benchmarks.csv

# از Excel
python tools/import-benchmarks.py --source benchmarks.xlsx

# از API
python tools/import-benchmarks.py --source api --url "..."
```

---

### 7. export-report.py
**تولید گزارش**

```bash
# خروجی PDF
python tools/export-report.py --format pdf --output report.pdf

# خروجی Excel
python tools/export-report.py --format excel --output report.xlsx

# خروجی HTML
python tools/export-report.py --format html --output report.html
```

---

## 🎯 نقشه راه توسعه

### Q1 2025
- [x] kpi_generator.py (در Root)
- [ ] kpi-validator-cli.py
- [ ] batch-generator.py
- [ ] search-kpis.py

### Q2 2025
- [ ] benchmark-analyzer.py
- [ ] data-quality-checker.py

### Q3 2025
- [ ] import-benchmarks.py
- [ ] export-report.py

---

## 🤝 مشارکت

می‌خواهید ابزاری بسازید؟

1. Fork کنید
2. Branch بسازید: `feature/tool-name`
3. کد بنویسید
4. تست کنید
5. Pull Request بزنید

[راهنمای مشارکت](../CONTRIBUTING.md)

---

## 📚 منابع

- [راهنمای کامل پروژه](../docs/overview.md)
- [مستندات API](../docs/api-documentation.md)

---

**نسخه:** 0.1.0  
**وضعیت:** در حال توسعه  
**تاریخ:** 2025-01-15
