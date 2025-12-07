# 🎨 Frontend - رابط کاربری

این پوشه شامل کد رابط کاربری (UI) و داشبورد پروژه است.

---

## 🏗️ ساختار
```
frontend/
├── public/                   ← فایل‌های استاتیک
│   ├── index.html
│   ├── favicon.ico
│   └── assets/
│
├── src/
│   ├── components/          ← کامپوننت‌های React
│   │   ├── Dashboard/
│   │   ├── KPIExplorer/
│   │   ├── BenchmarkView/
│   │   ├── ReportGenerator/
│   │   └── Common/
│   │
│   ├── pages/               ← صفحات اصلی
│   │   ├── Home.tsx
│   │   ├── KPILibrary.tsx
│   │   ├── CompanyProfile.tsx
│   │   ├── Benchmarking.tsx
│   │   └── Reports.tsx
│   │
│   ├── hooks/               ← Custom Hooks
│   │   ├── useKPIs.ts
│   │   ├── useBenchmarks.ts
│   │   └── useAuth.ts
│   │
│   ├── services/            ← API Calls
│   │   ├── api.ts
│   │   ├── kpiService.ts
│   │   └── benchmarkService.ts
│   │
│   ├── store/               ← State Management
│   │   ├── kpiSlice.ts
│   │   ├── userSlice.ts
│   │   └── store.ts
│   │
│   ├── utils/               ← Utilities
│   │   ├── helpers.ts
│   │   ├── validators.ts
│   │   └── formatters.ts
│   │
│   ├── types/               ← TypeScript Types
│   │   ├── kpi.types.ts
│   │   └── api.types.ts
│   │
│   ├── styles/              ← استایل‌ها
│   │   ├── globals.css
│   │   └── tailwind.config.js
│   │
│   ├── App.tsx              ← کامپوننت اصلی
│   ├── main.tsx             ← Entry Point
│   └── routes.tsx           ← مسیرها
│
├── tests/                    ← تست‌ها
├── package.json
├── tsconfig.json
└── vite.config.ts
```

---

## 🚀 Technology Stack

### Core
- **React 18+** - کتابخانه اصلی
- **TypeScript** - Type Safety
- **Vite** - Build Tool

### UI Framework
- **Tailwind CSS** - Styling
- **shadcn/ui** - Component Library
- **Lucide React** - Icons

### State Management
- **Redux Toolkit** - یا **Zustand**

### Data Fetching
- **TanStack Query** (React Query)

### Routing
- **React Router v6**

### Charts & Visualization
- **Recharts** - نمودارها
- **D3.js** - Visualizations پیشرفته

### Forms
- **React Hook Form**
- **Zod** - Validation

---

## 🎨 صفحات اصلی

### 1. Dashboard (داشبورد اصلی)
**مسیر:** `/dashboard`

**ویژگی‌ها:**
- نمای کلی شاخص‌های کلیدی
- نمودارهای روند
- هشدارها و اعلان‌ها
- مقایسه سریع با بنچمارک‌ها

**کامپوننت‌ها:**
```tsx
<Dashboard>
  <KPICards />
  <TrendCharts />
  <BenchmarkComparison />
  <Alerts />
</Dashboard>
```

---

### 2. KPI Library (کتابخانه شاخص‌ها)
**مسیر:** `/kpis`

**ویژگی‌ها:**
- مرور 90 شاخص EFQM 2025
- جستجو و فیلتر
- مشاهده جزئیات کامل
- امتیازهای SMART و RADAR

**کامپوننت‌ها:**
```tsx
<KPILibrary>
  <SearchBar />
  <FilterPanel />
  <KPIGrid />
  <KPIDetailModal />
</KPILibrary>
```

---

### 3. Benchmarking (بنچمارکینگ)
**مسیر:** `/benchmarking`

**ویژگی‌ها:**
- مقایسه با شرکت‌های اروپایی
- Gap Analysis
- نمودارهای مقایسه‌ای
- توصیه‌های بهبود

**کامپوننت‌ها:**
```tsx
<Benchmarking>
  <CompanySelector />
  <ComparisonChart />
  <GapAnalysis />
  <Recommendations />
</Benchmarking>
```

---

### 4. Reports (گزارش‌ها)
**مسیر:** `/reports`

**ویژگی‌ها:**
- تولید گزارش سفارشی
- خروجی PDF/Excel
- قالب‌های آماده
- زمان‌بندی خودکار

---

### 5. Company Profile (پروفایل شرکت)
**مسیر:** `/profile`

**ویژگی‌ها:**
- اطلاعات شرکت
- شاخص‌های فعال
- تاریخچه داده‌ها
- تنظیمات

---

## 🔧 نصب و اجرا (آینده)
```bash
# نصب وابستگی‌ها
cd frontend
npm install

# اجرای Development
npm run dev

# Build برای Production
npm run build

# Preview Build
npm run preview
```

---

## 🧪 تست
```bash
# Unit Tests
npm run test

# E2E Tests
npm run test:e2e

# Coverage
npm run test:coverage
```

---

## 🎨 طراحی UI/UX

### رنگ‌ها
```css
/* Primary */
--primary: #2563eb      /* آبی */
--primary-dark: #1e40af

/* Success */
--success: #16a34a      /* سبز */

/* Warning */
--warning: #f59e0b      /* نارنجی */

/* Danger */
--danger: #dc2626       /* قرمز */

/* Neutral */
--gray-50: #f9fafb
--gray-900: #111827
```

### Typography
- **فونت فارسی:** Vazirmatn
- **فونت انگلیسی:** Inter

---

## 📱 Responsive Design

- ✅ Desktop: 1920px+
- ✅ Laptop: 1366px - 1920px
- ✅ Tablet: 768px - 1366px
- ✅ Mobile: 320px - 768px

---

## 🎯 نقشه راه

### Q2 2025
- [ ] راه‌اندازی پروژه React + Vite
- [ ] صفحات اصلی (Dashboard, KPI Library)
- [ ] کامپوننت‌های پایه
- [ ] اتصال به Backend API

### Q3 2025
- [ ] صفحات پیشرفته (Benchmarking, Reports)
- [ ] نمودارها و Visualizations
- [ ] تست کامل
- [ ] بهینه‌سازی Performance

### Q4 2025
- [ ] راه‌اندازی عمومی
- [ ] Mobile App (React Native)
- [ ] PWA Support
- [ ] Dark Mode

---

## 🤝 مشارکت

برای توسعه Frontend:

1. Fork کنید
2. Feature Branch بسازید
3. کامپوننت بنویسید
4. تست کنید
5. Pull Request بزنید

**استانداردها:**
- ✅ TypeScript برای همه فایل‌ها
- ✅ Tailwind CSS برای استایل
- ✅ Component Documentation
- ✅ Unit Tests

---

## 📚 منابع

- [React Documentation](https://react.dev)
- [TypeScript](https://www.typescriptlang.org)
- [Tailwind CSS](https://tailwindcss.com)
- [shadcn/ui](https://ui.shadcn.com)

---

**نسخه:** 0.1.0  
**وضعیت:** برنامه‌ریزی شده  
**تاریخ:** 2025-01-15
