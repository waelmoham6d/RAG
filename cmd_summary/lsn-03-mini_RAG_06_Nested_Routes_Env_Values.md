# mini-RAG | 06 | Nested Routes + Env Values

## 1. الشرح التفصيلي للدرس (Step-by-Step Explanation)

### أ. الهدف المعماري (Architecture & Best Practices)
- **إبقاء `main.py` صغيراً (Minimal):** عدم إغراق الملف الرئيسي بجميع المسارات (Routes) واللوجيك الخاص بالتطبيق، حيث أن وضع كافة المسارات في مكان واحد يجعل التطبيق صعب الصيانة والتوسع مستقبلاً.
- **فصل المسارات في الموديولات:** تنظيم الكود عن طريق تقسيم المسارات داخل مجلد مخصص (`routes/`) وإنشاء ملفات مستقلة لكل مجموعة من المسارات المترابطة.

### ب. إنشاء مجلد المسارات وحزمة بايثون (`routes/`)
- إنشاء مجلد باسم `routes`.
- إضافة ملف `__init__.py` داخل المجلد ليتعرف بايثون عليه كـ Package / Module.

### ج. استخدام `APIRouter` في `routes/base.py`
- إنشاء ملف `base.py` داخل مجلد `routes` لإدارة المسارات الأساسية (مثل مسار الترحيب أو الـ Health Check).
- بدلاً من استخدام كائن `FastAPI()` الرئيسي، يتم استخدام `APIRouter` لتعريف راوتر فرعي.
- إضافة المسار وتغليفه بالدالة المناسبة.

### د. ربط المسارات الفرعية بالتطبيق الرئيسي `main.py`
- استيراد `base_router` في ملف `main.py`.
- تسجيل المسارات الفرعية في التطبيق الرئيسي باستخدام الأمر `app.include_router(base.base_router)`.

### هـ. تحسين وتنظيم المسارات (`prefix` و `tags`)
- **`prefix`:** إضافة بادئة موحدة لجميع المسارات التابعة للراوتر (مثل `/api/v1`) لتسهيل إدارة واستدعاء واجهات البرمجة (Endpoints).
- **`tags`:** استخدام الوسوم لتنسيق وتنظيم واجهة التوثيق التفاعلية (Swagger UI).

### و. إدارة متغيرات البيئة (`.env` Values)
- تثبيت مكتبة `python-dotenv`.
- استدعاء `load_dotenv()` في بداية التطبيق وقبل تحميل المسارات، لرفع قيم الملف `.env` إلى نظام متغيرات البيئة الخاص بالنظام (`os.environ`).
- قراءة القيم المخزنة مثل `APP_NAME` و `APP_VERSION` باستخدام `os.getenv()`.

### ز. الدوال غير المتزامنة (`async def`)
- الاعتماد على `async def` عند تعريف دوال المسارات لتعزيز أداء التطبيق والاستفادة من قابليات سيرفر Uvicorn في معالجة طلبات متعددة بالتوازي (Asynchronous Concurrency).

---

## 2. الأوامر البرمجية وشرحها التفصيلي (Commands Breakdown)

### أ. تثبيت مكتبة إدارة متغيرات البيئة
```bash
pip install python-dotenv
```
- **الشرح:** أمر تثبيت مكتبة `python-dotenv` باستخدام أداة إدارة حزم بايثون `pip` لقراءة المتغيرات المخزنة في ملف `.env`.

### ب. تشغيل خادم FastAPI
```bash
fastapi dev main.py
```
- **الشرح:**
  - `fastapi`: أداة السطر البرمجي الخاصة بـ FastAPI.
  - `dev`: تشغيل التطبيق في وضع التطوير (Development Mode) مع تفعيل خيار Re-load التلقائي عند تعديل الكود.
  - `main.py`: ملف مدخل التطبيق الذي يحتوي على كائن `FastAPI`.

---

## 3. الأكواد البرمجية (Code Snippets)

### أ. ملف المسار الأساسي `routes/base.py`
```python
import os
from fastapi import APIRouter

# تعريف كائن الراوتر مع تحديد البريفكس والتاجز
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def welcome():
    # قراءة المتغيرات من بيئة النظام
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    
    return {
        "app_name": app_name,
        "app_version": app_version
    }
```

### ب. ملف التطبيق الرئيسي `main.py`
```python
from fastapi import FastAPI
from dotenv import load_dotenv
from routes import base

# تحميل متغيرات البيئة أولاً قبل تحميل المسارات
load_dotenv(".env")

app = FastAPI()

# تضمين الراوتر الفرعي
app.include_router(base.base_router)
```

---

## 4. المسارات والروابط (URLs & Endpoints)

- **رابط التطوير المحلي (Local Server):** `http://127.0.0.1:8000` (أو Port 5000)
- **مسار الـ Endpoint الرئيسي:** `http://127.0.0.1:8000/api/v1/`
- **واجهة التوثيق Swagger UI:** `http://127.0.0.1:8000/docs`
- **واجهة التوثيق ReDoc:** `http://127.0.0.1:8000/redoc`
