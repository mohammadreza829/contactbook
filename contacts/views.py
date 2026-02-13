from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
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
