from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the contacts index.")

def contact_list(request):
    return render(request, 'contacts/contact_list.html')

