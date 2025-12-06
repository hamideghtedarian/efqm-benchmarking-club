# 📐 Data Models - مدل‌های داده

این پوشه شامل JSON Schema های استاندارد برای اعتبارسنجی داده‌ها است.

---

## 📊 مدل‌های موجود

### 1. kpi-schema.json
**توضیح:** Schema کامل برای اعتبارسنجی فایل‌های شاخص

**استفاده:**
```bash
# اعتبارسنجی یک شاخص
jsonschema -i R6-1-003.json data-models/kpi-schema.json
```

---

### 2. company-profile-schema.json
**توضیح:** Schema پروفایل شرکت

**فیلدهای اصلی:**
- company_id (required)
- company_name (required)
- industry (required)
- country (required)
- size (enum: Small, Medium, Large)
- efqm_recognition (optional)

---

### 3. data-entry-schema.json
**توضیح:** Schema ورود داده‌های واقعی شاخص

**فیلدهای اصلی:**
- kpi_code (required, pattern: R[6-7]-[1-5]-[0-9]{3})
- period (required, format: YYYY-QX or YYYY-MM)
- value (required, number)
- source (required)
- verified (boolean)

---

### 4. benchmark-schema.json
**توضیح:** Schema داده‌های بنچمارک

**ساختار:**
```json
{
  "company_id": "string",
  "data_year": 2024,
  "kpis": {
    "R6-1-001": 85.5,
    "R6-1-002": 62
  }
}
```

---

### 5. report-schema.json
**توضیح:** Schema گزارش‌های تحلیلی

---

## 🎯 نقشه راه

### Q2 2025
- [ ] kpi-schema.json
- [ ] company-profile-schema.json
- [ ] data-entry-schema.json

### Q3 2025
- [ ] benchmark-schema.json
- [ ] report-schema.json
- [ ] dashboard-config-schema.json

---

## 📚 استفاده

### نصب ابزار اعتبارسنجی
```bash
# Python
pip install jsonschema

# Node.js
npm install ajv
```

### مثال اعتبارسنجی (Python)
```python
import json
import jsonschema

# بارگذاری schema
with open('data-models/kpi-schema.json') as f:
    schema = json.load(f)

# بارگذاری داده
with open('R6-1-003.json') as f:
    data = json.load(f)

# اعتبارسنجی
jsonschema.validate(data, schema)
print("✅ Valid!")
```

### مثال اعتبارسنجی (Node.js)
```javascript
const Ajv = require('ajv');
const ajv = new Ajv();

const schema = require('./data-models/kpi-schema.json');
const data = require('./R6-1-003.json');

const validate = ajv.compile(schema);
const valid = validate(data);

if (valid) {
  console.log('✅ Valid!');
} else {
  console.log('❌ Invalid:', validate.errors);
}
```

---

## 🤝 مشارکت

می‌خواهید Schema جدیدی اضافه کنید؟

1. از [JSON Schema](https://json-schema.org/) استفاده کنید
2. مستندسازی کنید
3. نمونه‌های معتبر و نامعتبر اضافه کنید
4. Pull Request بزنید

---

**نسخه:** 0.1.0  
**وضعیت:** برنامه‌ریزی شده  
**تاریخ:** 2025-01-15
