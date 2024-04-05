from django.shortcuts import render

from .models import Service

# Create your views here.


def index(request):
    return render(request, "services/home.html")


def services_details(request, slug):
    service = Service.objects.filter(slug=slug)[0]
    return render(request, "services/details.html", {"service": service})
