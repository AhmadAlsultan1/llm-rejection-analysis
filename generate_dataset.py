import json
import random
from pathlib import Path

categories = {
    "missing_documents": [
        "لم يتم إرفاق الهوية الوطنية.",
        "المستند المطلوب غير موجود.",
        "المرفقات ناقصة.",
        "لم يتم رفع جميع الصفحات.",
        "الوثيقة المطلوبة غير مرفقة."
    ],
    "poor_quality": [
        "الصورة غير واضحة.",
        "جودة الصورة ضعيفة.",
        "المستند مصور بجودة منخفضة.",
        "لا يمكن قراءة البيانات بسبب ضبابية الصورة.",
        "الصورة مقصوصة ولا تظهر كامل المستند."
    ],
    "data_mismatch": [
        "رقم الهوية لا يطابق البيانات المدخلة.",
        "الاسم لا يطابق الهوية.",
        "تاريخ الميلاد مختلف عن الموجود في المستند.",
        "يوجد اختلاف في بيانات العميل.",
        "رقم الجوال لا يطابق الطلب."
    ],
    "expired_document": [
        "المستند منتهي الصلاحية.",
        "الهوية منتهية.",
        "الرخصة منتهية الصلاحية.",
        "الوثيقة غير سارية.",
        "تاريخ انتهاء المستند تجاوز المدة المسموحة."
    ],
    "insufficient_evidence": [
        "لا يوجد دليل كافٍ لإثبات الطلب.",
        "المرفقات لا تدعم المعلومات المدخلة.",
        "الإثبات المرفق غير كافٍ.",
        "البيانات غير مدعومة بوثائق.",
        "يلزم إرفاق مستند داعم."
    ],
    "incomplete_information": [
        "تم ترك بعض الحقول فارغة.",
        "البيانات غير مكتملة.",
        "لم يتم تعبئة جميع المعلومات المطلوبة.",
        "الطلب يحتوي على معلومات ناقصة.",
        "ينقص الطلب بعض التفاصيل الأساسية."
    ]
}

output = []

for _ in range(150):
    category = random.choice(list(categories.keys()))
    reason = random.choice(categories[category])
    output.append(reason)

random.shuffle(output)

Path("data").mkdir(exist_ok=True)

with open("data/rejection_reasons.json", "w", encoding="utf-8") as file:
    json.dump(output, file, ensure_ascii=False, indent=2)

print("Generated 150 Arabic rejection reasons.")