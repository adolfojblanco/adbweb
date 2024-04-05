from django.contrib import messages
from django.shortcuts import redirect, render

from applications.services.models import Service

from .forms import ContactForm


# Home View
def home(request):
    services = Service.objects.filter(is_active=True)
    return render(request, "home/index.html", {"services": services})


# Contact view
def contact(request):
    return render(request, "home/contact.html")


def create_post(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se envio correctamente el mensaje")
            return redirect("home:contact", {"form": form})
    else:
        form = ContactForm()

    return render(request, "home/contact.html", {"form": form})
