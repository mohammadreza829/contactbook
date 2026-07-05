# 📒 ContactBook — دفترچه مخاطبین با جنگو

یک پروژه ساده و تمرینی با **Django 6** برای مدیریت مخاطبین؛ ساخته‌شده بعد از ۵ جلسه کلاس جنگو 🙂

با این اپ می‌تونید مخاطب‌هاتون رو ببینید، جزئیات هر مخاطب رو باز کنید و مخاطب جدید اضافه کنید.

---

## ✨ امکانات

- 📋 **لیست مخاطبین** — نمایش همه مخاطب‌ها به‌صورت کارت، مرتب‌شده بر اساس تاریخ ساخت (جدیدترین اول)
- 👤 **جزئیات مخاطب** — نمایش نام، ایمیل، تلفن و آدرس هر مخاطب
- ➕ **افزودن مخاطب** — فرم ساخت مخاطب جدید با فرم HTML و متد POST
- 🎨 **قالب‌بندی با Template Inheritance** — قالب پایه (`base.html`) به‌همراه partial های جدا برای هدر، فوتر و نویگیشن
- 🗄️ **پنل ادمین جنگو** — مدیریت مخاطب‌ها از مسیر `/admin/`

---

## 🛠️ تکنولوژی‌ها

| ابزار | نسخه / توضیح |
|---|---|
| Python | 3.13 |
| Django | 6.0.2 |
| دیتابیس | SQLite (پیش‌فرض جنگو) |
| فرانت‌اند | HTML / CSS / کمی JavaScript |

---

## 📁 ساختار پروژه

```
contactbook/
├── ContactBook/            # تنظیمات اصلی پروژه
│   ├── settings.py
│   ├── urls.py             # مسیرهای اصلی (admin + include اپ contacts)
│   ├── wsgi.py / asgi.py
│   └── __init__.py
└── contacts/               # اپ اصلی مخاطبین
    ├── models.py           # مدل Contact
    ├── views.py            # ویوهای لیست، جزئیات و ساخت مخاطب
    ├── urls.py             # مسیرهای اپ
    ├── admin.py
    ├── migrations/
    ├── static/contacts/    # فایل‌های CSS و JS
    └── templates/
        ├── parent/base.html        # قالب پایه
        ├── partials/               # هدر، فوتر، نویگیشن
        ├── contacts/               # لیست و جزئیات مخاطب
        └── forms/contact_form.html # فرم افزودن مخاطب
```

---

## 🧩 مدل داده

```python
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200, default="unknown")
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
```

هر مخاطب به یک کاربر (`User`) وصله و مخاطب‌ها بر اساس `created_date` نزولی مرتب می‌شن.

---

## 🔗 مسیرها (URLs)

| مسیر | ویو | توضیح |
|---|---|---|
| `/` | `contact_list` | لیست همه مخاطب‌ها |
| `/create/` | `contact_create` | فرم افزودن مخاطب جدید |
| `/<id>/` | `contact_detail` | جزئیات یک مخاطب |
| `/admin/` | پنل ادمین | مدیریت داده‌ها |

---

## 🚀 راه‌اندازی و اجرا

### ۱. ساخت محیط مجازی و نصب جنگو

```bash
python -m venv venv

# ویندوز
venv\Scripts\activate

# لینوکس / مک
source venv/bin/activate

pip install django
```

### ۲. اجرای مایگریشن‌ها

```bash
python manage.py migrate
```

### ۳. ساخت کاربر

> ⚠️ **نکته مهم:** ویوها فعلاً مخاطب‌ها رو برای کاربری با یوزرنیم `mohammadreza` نشون می‌دن، پس حتماً کاربری با همین یوزرنیم بسازید:

```bash
python manage.py createsuperuser
# Username: mohammadreza
```

### ۴. اجرای سرور

```bash
python manage.py runserver
```

حالا برید به آدرس: **http://127.0.0.1:8000/** 🎉

---

## 📚 چیزهایی که تو این پروژه تمرین شده

- ساخت پروژه و اپ در جنگو (`startproject` و `startapp`)
- تعریف مدل و کار با ORM و مایگریشن‌ها
- ویوهای تابعی (Function-Based Views)
- مسیردهی با `urls.py` و `include`
- قالب‌ها، وراثت قالب (`extends` / `block`) و partial ها (`include`)
- کار با فرم HTML و متد `POST` و `redirect`
- فایل‌های استاتیک (CSS و JS)
- رابطه `ForeignKey` بین مخاطب و کاربر

---

## 🔮 ایده‌هایی برای قدم‌های بعدی

- [ ] استفاده از **Django Forms / ModelForm** به‌جای خوندن مستقیم `request.POST`
- [ ] اضافه کردن **لاگین و ثبت‌نام** تا هر کاربر مخاطب‌های خودش رو ببینه (به‌جای یوزرنیم ثابت)
- [ ] قابلیت **ویرایش و حذف** مخاطب
- [ ] **جستجو** بین مخاطب‌ها
- [ ] اعتبارسنجی شماره تلفن و ایمیل

---

> این پروژه یک تمرین آموزشی است و برای محیط پروداکشن آماده نیست (مثلاً `DEBUG=True` و `SECRET_KEY` داخل کد قرار دارد).
