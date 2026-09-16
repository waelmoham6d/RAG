# mini-RAG | 07 | Uploading a File (رفع الملفات وبناء مشروع مهيكل)

## 📌 ملخص الشرح التفصيلي (Detailed Step-by-Step Explanation)

يقدم هذا الدرس شرحاً عملياً وشاملاً لكيفية بناء خاصية رفع الملفات (File Upload) داخل تطبيق **FastAPI** بلغة **Python**، مع التركيز على **أفضل الممارسات الهندسية (Best Practices)** لترتيب وتنظيم الكود (Software Architecture) لضمان سهولة صيانته واختباره وتوسعه مستقبلاً.

---

### 1. إعادة هيكلة المشروع واستخدام البويلر بليت (Boilerplate & Directory Layout)
- **مفهوم الـ Boilerplate:** يُنصح دائماً عند البدء في أي مشروع بإطار عمل مثل FastAPI بالبحث عن نماذج جاهزة متفق عليها مجتمعياً (مثل `FastAPI boilerplate` على GitHub) لتجنب "إعادة اختراع العجلة" والبدء من هيكلية مجربة ومُعتمدة.
- **عزل كود التطبيق:** تم نقل كل كود اللوجيك الخاص بالبرنامج إلى مجلد رئيسي جديد يُدعى `src/` والإبقاء على الملفات التعريفية والمستندية في الـ Root (مثل `README.md` و `LICENSE`).
- **إدارة الإصدارات:** العمل على فرع محلي منفصل في Git باسم `07-tutorial` للحفاظ على استقرار الكود.

---

### 2. نمط التصميم (MVC Architecture Pattern)
لضمان الفصل الكامل بين المسؤوليات (Separation of Concerns)، يتبع المشروع نمط **MVC**:
- **Models (`src/models/`):** للتحكم في أنماط البيانات، الكائنات (Schemas)، والـ Enums.
- **Controllers (`src/controllers/`):** لاحتواء كافة المنطق البرمجي (Business Logic) وتفريغ الـ Routes منه تماماً لتسهيل اختبار الكود (Unit Testing).
- **Routes (`src/routes/`):** لاستقبال الطلبات البرمجية عبر الـ HTTP وتوجيهها للـ Controllers المناسبة دون تنفيذ أي منطق معقد بداخلها.
- **Helpers (`src/helpers/`):** للوظائف المساعدة الإضافية والإعدادات العامة التي تحتاجها كافة أجزاء النظام.
- **ملفات `__init__.py`:** وضع ملف `__init__.py` داخل كل مجلد لتحويله إلى `Python Package` وتسهيل عمليات الـ Import.

---

### 3. إدارة الإعدادات بواسطة Pydantic Settings
بدلاً من قراءة ملف الـ `.env` بطريقة تقليدية وغير آمنة (`load_dotenv`)، تم الاعتماد على مكتبة **Pydantic Settings** (`pydantic-settings`):
- تحويل إعدادات `.env` إلى Python Class يُدعى `Settings` يورث من `BaseSettings`.
- إجراء الـ Data Validation التلقائية على قيم الإعدادات قبل بدء التشغيل.
- إضافة قيم متقدمة للتحكم بالملفات المرفوعة:
  - `FILE_ALLOWED_TYPES`: قائمة بالأنواع المسموح بها (مثل `text/plain` و `application/pdf`).
  - `FILE_MAX_SIZE`: الحد الأقصى لحجم الملف بالميجابايت (مثلاً `10MB`).
  - `FILE_DEFAULT_CHUNK_SIZE`: حجم الشريحة عند قراءة الملف من الميموري (مثل `512KB`).

---

### 4. حقن التبعيات (Dependency Injection)
- استخدام `Depends` من `fastapi` لتمرير الإعدادات `get_settings` كـ Dependency للـ Routes والـ Controllers.
- يرفع ذلك من كفاءة الأداء ويجعل الـ Functions مرنة للغاية وجاهزة للـ Testing والـ Mocking بسهولة.

---

### 5. التحقق من صحة الملفات (File Validation Logic)
تم بناء دالة فحص وتدقيق `validate_uploaded_file` في الـ `DataController` للتأكد من المحددات التالية:
1. **التحقق من الـ MIME Type:** مطابقة `file.content_type` بالقائمة المسموحة.
2. **التحقق من حجم الملف:** ضرب الحد الأقصى المُدخل في `.env` (بالـ MB) في `1024 * 1024` لتحويله إلى Bytes لمقارنته بحجم الملف الفعلي `file.size`.

---

### 6. توحيد الإشارات والـ HTTP Status Codes باستخدام Enums
- بدلاً من إرجاع قيم عشوائية، تم بناء كلاس `ResponseSignal` يورث من `Enum` داخل `src/models/enums/`.
- توحيد رموز الاستجابة بأسماء ثابتة: `FILE_TYPE_NOT_SUPPORTED`, `FILE_SIZE_EXCEEDED`, `FILE_UPLOAD_SUCCESS`, `FILE_UPLOAD_FAILED`.
- استخدام `JSONResponse` مع توفير الـ **HTTP Status Code** الصحيح (مثل `400 Bad Request` عند وجود خطأ في المدخلات، و `200 OK` في حالة النجاح).

---

### 7. التنظيم الهيكلي والمشاريع المتعددة (Multi-Tenancy Architecture)
- الاعتماد على مفهوم **Tenant / Project ID**: تنظيم الملفات بحيث تُرفع تحت مجلد مخصص لكل مشروع على حدة.
- إنشاء `BaseController` ليحتوي على الجذور المسؤولة عن الحصول على المسار المطلق لمجلد المشروع باستعمال مكتبة `os`.
- إعداد دالة `get_project_path(project_id)` لإنشاء المجلد المخصص داخل `src/assets/files/{project_id}` تلقائياً إذا لم يكن متواخداً.

---

### 8. تطهير وإنشاء أسماء ملفات فريدة (Sanitization & Unique Names)
لحماية النظام ضد الثغرات وأخطاء الكتابة فوق الملفات المسجلة بنفس الاسم:
- إنشاء دالة توليد نص عشوائي مكون من 12 حرفاً ورقماً.
- استخدام **Regex (`re`)** لتطهير الاسم الأصلي وحذف كل الرموز والمسافات وإبقاء النقاط والشرطات السفلية فقط.
- الدمج بين الاسم العشوائي والاسم المُنظف والفحص المستمر باستخدام `os.path.exists()` لتفادي التكرار.

---

### 9. رفع الملفات بالشرائح (Chunked Asynchronous Streaming)
- قراءة الملفات الضخمة مرة واحدة في الميموري يُعرض السيرفر للسقوط والبطء الشديد عند استخدام الخدمة بكثرة.
- الاعتماد على مكتبة **`aiofiles`** لقراءة الملف قطعة تلو الأخرى (`chunks`) بحجم الشريحة المحددة (مثلاً `512KB`) ثم كتابته عبر الباينري موجه (`wb`) للقرص الصعب.

---

### 10. حماية البيانات وتسجيل الأخطاء (Logging & Error Handling)
- استخدام مكتبة `logging` للحصول على الـ `logger` التابع لـ `uvicorn.error`.
- الاحتفاظ بـ Stack Trace والتفاصيل الحساسة للخطأ داخل الـ Logs الخاصة بالآدمن فقط.
- إرسال رسالة عامة وآمنة للمستخدم النهائي دون كشف أي بنية تتبع سيرفرية قد تُستغل في ثغرات أمنية.

---

## 💻 استخراج وشرح جميع الأوامر (Commands Breakdown)

### أوامر الـ Terminal / Bash

```bash
# 1. إنشاء فرع جديد في Git والتحول إليه للبدء في الدرس السابع
git checkout -b 07-tutorial

# 2. الانتقال إلى مجلد الكود الرئيسي
cd src

# 3. تثبيت مكتبة aiofiles الخاصة بالتعامل غير المتزامن مع الملفات
pip install aiofiles

# 4. تشغيل خادم Uvicorn مع التحديث التلقائي للتغييرات
uvicorn main:app --reload
```

---

## ⚙️ كود وملفات المشروع (Code Snippets & Architecture)

### 1. هيكل المجلدات (Project Structure)
```text
mini-rag/
├── LICENSE
├── README.md
├── requirements.txt
└── src/
    ├── __init__.py
    ├── main.py
    ├── assets/
    │   └── files/          # مجلد تخزين الملفات المرفوعة مقسمة حسب project_id
    ├── controllers/
    │   ├── __init__.py
    │   ├── BaseController.py
    │   ├── DataController.py
    │   └── ProjectController.py
    ├── helpers/
    │   ├── __init__.py
    │   └── config.py
    ├── models/
    │   ├── __init__.py
    │   └── enums/
    │       ├── __init__.py
    │       └── ResponseEnums.py
    └── routes/
        ├── __init__.py
        ├── base.py
        └── data.py
```

### 2. ملف الإعدادات `src/helpers/config.py`
```python
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache()
def get_settings():
    return Settings()
```

### 3. ملف رموز الاستجابة `src/models/enums/ResponseEnums.py`
```python
from enum import Enum

class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
```

### 4. كود تطهير وتمرير أسماء الملفات `src/controllers/DataController.py`
```python
import re
import random
import string

def generate_random_string(length: int = 12) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def get_clean_file_name(original_file_name: str) -> str:
    clean_name = re.sub(r'[^\w\.\-]', '_', original_file_name)
    clean_name = re.sub(r'\s+', '_', clean_name)
    return clean_name
```

### 5. رفع الملفات وحفظها بالشرائح (`aiofiles`)
```python
import aiofiles

async def save_file_chunks(file_object, destination_path: str, chunk_size: int):
    async with aiofiles.open(destination_path, 'wb') as out_file:
        while chunk := await file_object.read(chunk_size):
            await out_file.write(chunk)
```

---

## 🌐 العناوين المحلية والروابط المذكورة (Local URLs & Ports)

- **رابط وثائق التفاعل Swagger UI:**  
  `http://localhost:5000/docs` أو `http://127.0.0.1:8000/docs`
- **رابط نقطة النهاية الخاصة برفع الملفات (POST Endpoint):**  
  `POST http://localhost:5000/api/v1/data/upload/{project_id}`
- **طريقة الإرسال في برنامج Postman:**
  - **HTTP Method:** `POST`
  - **Body Format:** `form-data`
  - **Key Name:** `file` (تغيير نوع الـ Key من Text إلى File واختيار الملف من الجهاز)
