from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .forms import ContactForm


# Home View
def home(request):
    return render(request, "home/index.html")


# Contact view
def contact(request):
    return render(request, "home/contact.html")


def create_post(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, "Se envio correctamente el mensaje")
            return render(request, "home/contact.html", {"form": form})

    else:
        form = ContactForm()

    return render(request, "home/contact.html", {"form": form})
