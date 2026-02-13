from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the contacts index.")


@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, "contacts/contact_list.html", {"contacts": contacts})


@login_required
def contact_detail(request, id):
    contact = get_object_or_404(Contact, id=id, user=request.user)
    return render(request, "contacts/contact_detail.html", {"contact": contact})


@login_required
def contact_create(request):
    if request.method == "POST":
        # داده‌ها از فرم HTML میاد
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        # ساختن مخاطب در دیتابیس
        contact = Contact.objects.create(
            user=request.user,
            name=name,
            email=email,
            phone=phone,
            address=address if address else "unknown",
        )

        # بعد از ذخیره، برو به صفحه detail همان مخاطب
        return redirect("contact_detail", id=contact.id)

    # اگر GET بود، فقط فرم خالی را نشان بده
    return render(request, "forms/contact_form.html")
