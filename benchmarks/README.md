# 🌍 Benchmarks - بنچمارک‌ها

این پوشه شامل داده‌های بنچمارک از شرکت‌های برتر اروپایی و استانداردهای جهانی است.

---

## 📊 ساختار
```
benchmarks/
├── european-leaders/          ← شرکت‌های برتر اروپایی
│   ├── germany/              ← آلمان
│   ├── uk/                   ← بریتانیا
│   ├── france/               ← فرانسه
│   ├── netherlands/          ← هلند
│   └── switzerland/          ← سوئیس
│
├── industry-averages/         ← میانگین‌های صنعتی
│   ├── manufacturing.json
│   ├── services.json
│   ├── technology.json
│   └── healthcare.json
│
└── world-class/              ← استانداردهای جهانی
    └── best-practices.json
```

---

## 🎯 شرکت‌های هدف (60+ شرکت)

### 🇩🇪 آلمان (15 شرکت)
- Siemens, BMW, Bosch, SAP, Volkswagen
- Mercedes-Benz, Deutsche Telekom, BASF
- Allianz, Deutsche Bank, Adidas
- Bayer, Porsche, Audi, Continental

### 🇬🇧 بریتانیا (12 شرکت)
- Rolls-Royce, GSK, Unilever, BP
- HSBC, Tesco, Vodafone, BT Group
- British Airways, BAE Systems, Diageo, AstraZeneca

### 🇫🇷 فرانسه (10 شرکت)
- Airbus, L'Oréal, Schneider Electric
- Total, Renault, Danone, LVMH
- Michelin, Sanofi, Orange

### 🇳🇱 هلند (8 شرکت)
- Philips, ING, Shell, ASML
- Heineken, Unilever, KPN, ABN AMRO

### 🇨🇭 سوئیس (8 شرکت)
- Nestlé, Novartis, Roche, ABB
- UBS, Credit Suisse, Zurich Insurance, Swatch

### سایر کشورها (7+ شرکت)
- 🇸🇪 Volvo, Ericsson, H&M
- 🇮🇹 Ferrari, Pirelli
- 🇪🇸 Santander, Telefónica

---

## 📈 داده‌های موجود

**وضعیت فعلی:** در حال جمع‌آوری 🔨

**منابع داده:**
- EFQM Recognition Database
- گزارش‌های سالانه عمومی شرکت‌ها
- تحقیقات بازار و صنعت
- دیتابیس‌های تحقیقاتی

---

## 🔮 برنامه Q2 2025

- [ ] جمع‌آوری داده 20 شرکت اول
- [ ] ایجاد فرمت استاندارد JSON
- [ ] اعتبارسنجی داده‌ها
- [ ] انتشار نسخه اول

---

## 📚 فرمت داده

نمونه فایل بنچمارک:
```json
{
  "company_id": "SIEMENS-DE-001",
  "company_name": "Siemens AG",
  "country": "Germany",
  "industry": "Manufacturing - Diversified",
  "size": "Large (300,000+ employees)",
  "efqm_recognition": "Recognised for Excellence 5*",
  "data_year": 2024,
  "kpis": {
    "R6-1-001": 87.5,
    "R6-1-002": 65,
    "R6-1-003": 88
  }
}
```

---

**نسخه:** 0.1.0  
**وضعیت:** در حال توسعه  
**تاریخ:** 2025-01-15
