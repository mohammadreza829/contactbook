# 📒 ContactBook — دفترچه مخاطبین با جنگو

یک پروژه‌ی کوچک و تمرینی با **Django 6** برای مدیریت مخاطب‌ها؛ چیزی که بعد از چند جلسه‌ی اول کلاس جنگو ساختم تا مفاهیم پایه رو دست خودم بیاد 🙂

با این اپ می‌تونید لیست مخاطب‌هاتون رو ببینید، جزئیات هرکدوم رو باز کنید و مخاطب جدید اضافه کنید. عمداً ساده نگهش داشتم؛ هدفم یاد گرفتن بود، نه ساختن یه محصول کامل.

---

## ✨ امکانات

- 📋 **لیست مخاطبین** — نمایش همه‌ی مخاطب‌ها به‌صورت کارت، مرتب‌شده بر اساس تاریخ ساخت (جدیدترین اول)
- 👤 **جزئیات مخاطب** — نام، ایمیل، تلفن و آدرس هر مخاطب
- ➕ **افزودن مخاطب** — فرم ساخت مخاطب جدید با فرم HTML و متد POST
- 🎨 **وراثت قالب** — یک قالب پایه (`base.html`) به‌همراه partial های جدا برای هدر، فوتر و نویگیشن
- 🗄️ **پنل ادمین جنگو** — مدیریت مخاطب‌ها از مسیر `/admin/`

---

## 🛠️ تکنولوژی‌ها

| ابزار | نسخه / توضیح |
|---|---|
| Python | 3.13 |
| Django | 6.0.2 |
| دیتابیس | SQLite (پیش‌فرض جنگو) |
| فرانت‌اند | HTML / CSS و کمی JavaScript |

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
| `/` | `contact_list` | لیست همه‌ی مخاطب‌ها |
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

> ⚠️ **نکته:** ویوها فعلاً مخاطب‌ها رو برای کاربری با یوزرنیم `mohammadreza` نشون می‌دن (این رو موقع یادگیری هاردکد کردم و هنوز درستش نکردم)، پس فعلاً حتماً کاربری با همین یوزرنیم بسازید:

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

## 📚 چیزهایی که تو این پروژه تمرین کردم

- ساخت پروژه و اپ در جنگو (`startproject` و `startapp`)
- تعریف مدل و کار با ORM و مایگریشن‌ها
- ویوهای تابعی (Function-Based Views)
- مسیردهی با `urls.py` و `include`
- قالب‌ها، وراثت قالب (`extends` / `block`) و partial ها (`include`)
- کار با فرم HTML و متد `POST` و `redirect`
- سرو کردن فایل‌های استاتیک (CSS و JS)
- رابطه‌ی `ForeignKey` بین مخاطب و کاربر

---

## 🔮 قدم‌های بعدی که تو ذهنم دارم

- [ ] استفاده از **Django Forms / ModelForm** به‌جای خوندن مستقیم `request.POST`
- [ ] اضافه کردن **لاگین و ثبت‌نام** تا هر کاربر مخاطب‌های خودش رو ببینه (به‌جای یوزرنیم ثابت)
- [ ] قابلیت **ویرایش و حذف** مخاطب
- [ ] **جستجو** بین مخاطب‌ها
- [ ] اعتبارسنجی شماره تلفن و ایمیل

---

> این پروژه یک تمرین آموزشیه و برای پروداکشن آماده نیست (مثلاً `DEBUG=True` و `SECRET_KEY` هنوز داخل کد قرار داره).
