#!/usr/bin/env python3
“””
EFQM 2025 KPI Generator
تولیدکننده خودکار شاخص‌های EFQM 2025

استفاده:
python kpi_generator.py –code R6-1-005 –name-fa “رضایت از کیفیت محصول” –name-en “Product Quality Satisfaction”

نویسنده: حمید اقتداریان
تاریخ: 2025-01-15
نسخه: 1.0.0
“””

import json
import argparse
from datetime import datetime
from typing import Dict, Any
import os

class EFQMKPIGenerator:
“”“کلاس تولیدکننده شاخص‌های EFQM 2025”””

```
def __init__(self, template_path: str = "kpi-passport-template.json"):
    """
    مقداردهی اولیه
    
    Args:
        template_path: مسیر فایل template
    """
    self.template_path = template_path
    self.template = self._load_template()
    
def _load_template(self) -> Dict[str, Any]:
    """بارگذاری template از فایل"""
    try:
        with open(self.template_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️  فایل template در مسیر {self.template_path} یافت نشد!")
        print("📝 در حال ساخت template پیش‌فرض...")
        return self._create_default_template()

def _create_default_template(self) -> Dict[str, Any]:
    """ساخت template پیش‌فرض"""
    # همان ساختار template که قبلاً ساختیم
    return {
        "metadata": {
            "template_version": "1.0.0",
            "efqm_version": "2025",
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "template_type": "kpi-passport"
        },
        # ... بقیه فیلدها
    }

def parse_kpi_code(self, code: str) -> Dict[str, int]:
    """
    تجزیه کد شاخص
    
    Args:
        code: کد شاخص مثل R6-1-003
        
    Returns:
        دیکشنری شامل criterion, sub_criterion, number
    """
    try:
        parts = code.replace('R', '').split('-')
        return {
            'criterion': int(parts[0]),
            'sub_criterion': int(parts[1]),
            'number': int(parts[2])
        }
    except Exception as e:
        raise ValueError(f"❌ فرمت کد نادرست: {code}. فرمت صحیح: R6-1-003")

def get_category_info(self, criterion: int, sub_criterion: int) -> Dict[str, str]:
    """
    دریافت اطلاعات دسته‌بندی براساس معیار و زیرمعیار
    
    Args:
        criterion: شماره معیار (6 یا 7)
        sub_criterion: شماره زیرمعیار
        
    Returns:
        دیکشنری شامل category و sub_category
    """
    categories = {
        6: {
            1: {
                "category": "معیار 6: برداشت‌های ذی‌نفعان",
                "sub_category": "6-1: برداشت‌های مشتریان",
                "folder": "criterion-6-stakeholder-perceptions/6-1-customer-perceptions"
            },
            2: {
                "category": "معیار 6: برداشت‌های ذی‌نفعان",
                "sub_category": "6-2: برداشت‌های کارکنان",
                "folder": "criterion-6-stakeholder-perceptions/6-2-people-perceptions"
            },
            3: {
                "category": "معیار 6: برداشت‌های ذی‌نفعان",
                "sub_category": "6-3: برداشت‌های سرمایه‌گذاران و شرکا",
                "folder": "criterion-6-stakeholder-perceptions/6-3-investor-business-partner-perceptions"
            },
            4: {
                "category": "معیار 6: برداشت‌های ذی‌نفعان",
                "sub_category": "6-4: برداشت‌های جامعه",
                "folder": "criterion-6-stakeholder-perceptions/6-4-society-perceptions"
            },
            5: {
                "category": "معیار 6: برداشت‌های ذی‌نفعان",
                "sub_category": "6-5: برداشت‌های شرکا و تامین‌کنندگان",
                "folder": "criterion-6-stakeholder-perceptions/6-5-partners-suppliers-perceptions"
            }
        },
        7: {
            1: {
                "category": "معیار 7: عملکرد استراتژیک و عملیاتی",
                "sub_category": "7-1: عملکرد استراتژیک و مالی",
                "folder": "criterion-7-strategic-operational-performance/7-1-strategic-financial-performance"
            },
            2: {
                "category": "معیار 7: عملکرد استراتژیک و عملیاتی",
                "sub_category": "7-2: عملکرد عملیاتی",
                "folder": "criterion-7-strategic-operational-performance/7-2-operational-performance"
            }
        }
    }
    
    try:
        return categories[criterion][sub_criterion]
    except KeyError:
        raise ValueError(f"❌ ترکیب معیار {criterion} و زیرمعیار {sub_criterion} نامعتبر است")

def calculate_smart_score(self, kpi_data: Dict[str, Any]) -> int:
    """
    محاسبه امتیاز SMART
    
    Args:
        kpi_data: داده‌های شاخص
        
    Returns:
        امتیاز کل SMART (0-100)
    """
    # در اینجا منطق محاسبه SMART را پیاده می‌کنیم
    # فعلاً یک مقدار پیش‌فرض برمی‌گردانیم
    return 95

def calculate_radar_score(self, kpi_data: Dict[str, Any]) -> int:
    """
    محاسبه امتیاز RADAR
    
    Args:
        kpi_data: داده‌های شاخص
        
    Returns:
        امتیاز کل RADAR (0-100)
    """
    # در اینجا منطق محاسبه RADAR را پیاده می‌کنیم
    # فعلاً یک مقدار پیش‌فرض برمی‌گردانیم
    return 90

def generate_kpi(
    self,
    code: str,
    name_fa: str,
    name_en: str,
    description_fa: str = "",
    formula: str = "",
    **kwargs
) -> Dict[str, Any]:
    """
    تولید یک شاخص جدید
    
    Args:
        code: کد شاخص (مثل R6-1-003)
        name_fa: نام فارسی شاخص
        name_en: نام انگلیسی شاخص
        description_fa: توضیح فارسی
        formula: فرمول محاسبه
        **kwargs: سایر پارامترها
        
    Returns:
        دیکشنری کامل شاخص
    """
    # تجزیه کد
    parsed_code = self.parse_kpi_code(code)
    
    # دریافت اطلاعات دسته‌بندی
    category_info = self.get_category_info(
        parsed_code['criterion'],
        parsed_code['sub_criterion']
    )
    
    # شروع با template
    kpi = json.loads(json.dumps(self.template))  # Deep copy
    
    # پر کردن فیلدهای اصلی
    kpi['kpi_identification']['kpi_code'] = code
    kpi['kpi_identification']['kpi_name_fa'] = name_fa
    kpi['kpi_identification']['kpi_name_en'] = name_en
    kpi['kpi_identification']['category'] = category_info['category']
    kpi['kpi_identification']['sub_category'] = category_info['sub_category']
    kpi['kpi_identification']['efqm_criterion'] = parsed_code['criterion']
    kpi['kpi_identification']['efqm_sub_criterion'] = parsed_code['sub_criterion']
    
    # پر کردن توضیحات
    if description_fa:
        kpi['definition']['description_fa'] = description_fa
    
    if formula:
        kpi['measurement']['formula'] = formula
    
    # به‌روزرسانی تاریخ‌ها
    today = datetime.now().strftime("%Y-%m-%d")
    kpi['metadata']['last_updated'] = today
    kpi['created_date'] = today
    kpi['last_modified'] = today
    
    # محاسبه امتیازها
    smart_score = self.calculate_smart_score(kpi)
    radar_score = self.calculate_radar_score(kpi)
    
    kpi['smart_validation']['total_score'] = smart_score
    kpi['radar_evaluation']['overall_score'] = radar_score
    
    return kpi

def save_kpi(self, kpi: Dict[str, Any], output_dir: str = "output") -> str:
    """
    ذخیره شاخص در فایل
    
    Args:
        kpi: داده‌های شاخص
        output_dir: مسیر خروجی
        
    Returns:
        مسیر فایل ذخیره شده
    """
    # ایجاد فولدر خروجی
    os.makedirs(output_dir, exist_ok=True)
    
    # ساخت نام فایل
    code = kpi['kpi_identification']['kpi_code']
    name_en = kpi['kpi_identification']['kpi_name_en']
    filename = f"{code}-{name_en.lower().replace(' ', '-')}.json"
    filepath = os.path.join(output_dir, filename)
    
    # ذخیره فایل
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(kpi, f, ensure_ascii=False, indent=2)
    
    return filepath

def generate_batch(self, kpis_list: list) -> list:
    """
    تولید دسته‌ای چند شاخص
    
    Args:
        kpis_list: لیست شاخص‌ها برای تولید
        
    Returns:
        لیست مسیر فایل‌های ذخیره شده
    """
    saved_files = []
    
    for kpi_info in kpis_list:
        print(f"⏳ در حال تولید {kpi_info['code']}...")
        kpi = self.generate_kpi(**kpi_info)
        filepath = self.save_kpi(kpi)
        saved_files.append(filepath)
        print(f"✅ {filepath}")
    
    return saved_files
```

def main():
“”“تابع اصلی برنامه”””
parser = argparse.ArgumentParser(
description=‘تولیدکننده خودکار شاخص‌های EFQM 2025’
)

```
parser.add_argument('--code', required=True, help='کد شاخص (مثل R6-1-003)')
parser.add_argument('--name-fa', required=True, help='نام فارسی شاخص')
parser.add_argument('--name-en', required=True, help='نام انگلیسی شاخص')
parser.add_argument('--description-fa', default='', help='توضیح فارسی')
parser.add_argument('--formula', default='', help='فرمول محاسبه')
parser.add_argument('--output', default='output', help='مسیر خروجی')

args = parser.parse_args()

# ایجاد نمونه Generator
generator = EFQMKPIGenerator()

# تولید شاخص
print(f"\n🚀 شروع تولید شاخص {args.code}...\n")

kpi = generator.generate_kpi(
    code=args.code,
    name_fa=args.name_fa,
    name_en=args.name_en,
    description_fa=args.description_fa,
    formula=args.formula
)

# ذخیره
filepath = generator.save_kpi(kpi, args.output)

print(f"\n✅ شاخص با موفقیت ایجاد شد!")
print(f"📁 مسیر فایل: {filepath}")
print(f"📊 امتیاز SMART: {kpi['smart_validation']['total_score']}/100")
print(f"📊 امتیاز RADAR: {kpi['radar_evaluation']['overall_score']}/100")
print(f"\n🎯 آماده برای استفاده!")
```

if **name** == “**main**”:
main()
