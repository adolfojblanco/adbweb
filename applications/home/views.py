from django.shortcuts import render


# Home View
def home(request):
    return render(request, "home/index.html")


# Contact view
def contact(request):
    return render(request, "home/contact.html")
