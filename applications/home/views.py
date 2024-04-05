from django.contrib import messages
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from applications.services.models import Service
from django.conf import settings
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
            email = request.POST['email']
            context = {'email': email}
            template = get_template('emails/contact.html')
            content = template.render(context)
            try:
                email = EmailMultiAlternatives(
                    'Registro de Usuario - Admin Otreze',
                    'Admin Otreze',
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                email.attach_alternative(content, 'text/html')
                email.send()

            except Exception as e:
                print(e)
            messages.success(request, "Se envio correctamente el mensaje")
            return redirect("home:index")
    else:
        form = ContactForm()
    return render(request, "home/contact.html", {"form": form})
