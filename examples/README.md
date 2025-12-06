# 📚 Examples - مثال‌های کاربردی

این پوشه شامل مثال‌های عملی برای استفاده از پروژه است.

---

## 📂 دسته‌بندی مثال‌ها

### 1. کار با شاخص‌ها

#### `complete-kpi-example.json`
**توضیح:** یک شاخص کامل با تمام فیلدها

**محتوا:**
- تمام 50+ فیلد پر شده
- SMART Score: 98/100
- RADAR Score: 94/100
- بنچمارک‌های واقعی

**استفاده:**
```bash
# مشاهده فایل
cat examples/complete-kpi-example.json

# استفاده به عنوان الگو
cp examples/complete-kpi-example.json my-new-kpi.json
```

---

#### `minimal-kpi-example.json`
**توضیح:** شاخص با حداقل فیلدهای الزامی

**فیلدهای الزامی:**
- kpi_code
- kpi_name_fa, kpi_name_en
- formula
- unit
- benchmarks

---

### 2. ورود داده

#### `data-entry-example.json`
**توضیح:** نمونه ورود داده واقعی
```json
{
  "company_id": "COMP-001",
  "kpi_code": "R6-1-001",
  "period": "2024-Q4",
  "value": 85.5,
  "source": "Customer Survey - December 2024",
  "sample_size": 500,
  "verified": true,
  "notes": "نظرسنجی آنلاین با 500 مشتری"
}
```

---

#### `batch-data-entry.json`
**توضیح:** ورود دسته‌ای چند شاخص
```json
{
  "company_id": "COMP-001",
  "period": "2024-Q4",
  "entries": [
    {"kpi_code": "R6-1-001", "value": 85.5},
    {"kpi_code": "R6-1-002", "value": 62},
    {"kpi_code": "R6-1-003", "value": 88}
  ]
}
```

---

### 3. پروفایل شرکت

#### `company-profile-example.json`
**توضیح:** نمونه پروفایل شرکت
```json
{
  "company_id": "COMP-001",
  "name": "شرکت نمونه صنعتی",
  "name_en": "Sample Industrial Company",
  "industry": "Manufacturing - Automotive",
  "sub_industry": "Auto Parts",
  "size": "Large",
  "employees": 5000,
  "revenue_million_usd": 500,
  "country": "Iran",
  "city": "تهران",
  "founded_year": 1990,
  "efqm_recognition": null,
  "contact": {
    "email": "info@sample.com",
    "website": "https://sample.com"
  }
}
```

---

### 4. داشبورد و گزارش‌ها

#### `dashboard-config-example.json`
**توضیح:** تنظیمات داشبورد شخصی
```json
{
  "dashboard_name": "Executive Dashboard",
  "widgets": [
    {
      "type": "gauge",
      "kpi_code": "R6-1-001",
      "position": {"x": 0, "y": 0, "w": 2, "h": 2}
    },
    {
      "type": "trend",
      "kpi_code": "R6-1-003",
      "periods": 12,
      "position": {"x": 2, "y": 0, "w": 4, "h": 2}
    }
  ]
}
```

---

#### `report-template-example.json`
**توضیح:** قالب گزارش سه‌ماهه

---

### 5. بنچمارکینگ

#### `benchmark-comparison-example.json`
**توضیح:** مقایسه با رقبا
```json
{
  "company_id": "COMP-001",
  "comparison_date": "2024-Q4",
  "kpi_code": "R6-1-001",
  "your_value": 82,
  "benchmarks": {
    "industry_average": 78,
    "top_quartile": 90,
    "competitor_a": 85,
    "competitor_b": 80
  },
  "gap_analysis": {
    "vs_industry": "+4",
    "vs_top_quartile": "-8",
    "vs_best_competitor": "-3"
  }
}
```

---

### 6. استفاده از API

#### `api-usage-example.py`
**توضیح:** مثال استفاده از API با Python
```python
import requests

# دریافت لیست شاخص‌ها
response = requests.get('http://api.efqm-club.org/v1/kpis')
kpis = response.json()

# دریافت یک شاخص خاص
kpi = requests.get('http://api.efqm-club.org/v1/kpis/R6-1-001')
print(kpi.json())

# ثبت داده جدید
data = {
    "kpi_code": "R6-1-001",
    "value": 85.5,
    "period": "2024-Q4"
}
response = requests.post(
    'http://api.efqm-club.org/v1/data',
    json=data
)
```

---

#### `api-usage-example.js`
**توضیح:** مثال استفاده از API با JavaScript
```javascript
// دریافت شاخص
fetch('http://api.efqm-club.org/v1/kpis/R6-1-001')
  .then(res => res.json())
  .then(data => console.log(data));

// ثبت داده
fetch('http://api.efqm-club.org/v1/data', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    kpi_code: 'R6-1-001',
    value: 85.5,
    period: '2024-Q4'
  })
});
```

---

## 🎯 نقشه راه

### Q2 2025
- [ ] complete-kpi-example.json
- [ ] data-entry-example.json
- [ ] company-profile-example.json

### Q3 2025
- [ ] dashboard-config-example.json
- [ ] benchmark-comparison-example.json
- [ ] api-usage-example.py
- [ ] api-usage-example.js

---

## 🤝 استفاده

### کپی کردن مثال
```bash
# کپی مثال کامل
cp examples/complete-kpi-example.json my-kpi.json

# ویرایش
nano my-kpi.json

# اعتبارسنجی
python tools/kpi-validator-cli.py --file my-kpi.json
```

---

## 📚 منابع

- [راهنمای شروع سریع](../QUICK-START.md)
- [مستندات API](../docs/api-documentation.md)
- [استانداردهای شاخص](../docs/kpi-standards.md)

---

**نسخه:** 0.1.0  
**وضعیت:** برنامه‌ریزی شده  
**تاریخ:** 2025-01-15
