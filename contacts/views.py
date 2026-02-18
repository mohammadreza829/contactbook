from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Contact

def index(request):
    return HttpResponse("Hello, world. You're at the contacts index.")

def contact_list(request):
    owner = get_object_or_404(User, username="mohammadreza")
    contacts = Contact.objects.filter(user=owner)
    return render(request, "contacts/contact_list.html", {"contacts": contacts})

def contact_detail(request, id):
    owner = get_object_or_404(User, username="mohammadreza")
    contact = get_object_or_404(Contact, id=id, user=owner)
    return render(request, "contacts/contact_detail.html", {"contact": contact})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Contact

OWNER_USERNAME = "mohammadreza"

def contact_create(request):
    owner = get_object_or_404(User, username=OWNER_USERNAME)

    if request.method == "POST":
        Contact.objects.create(
            user=owner,
            name=request.POST.get("name", "").strip(),
            email=request.POST.get("email", "").strip(),
            phone=request.POST.get("phone", "").strip(),
            address=request.POST.get("address", "").strip() or "unknown",
        )
        return redirect("contact_list")

    return render(request, "forms/contact_form.html")
