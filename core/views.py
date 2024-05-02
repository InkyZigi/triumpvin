from django.shortcuts import render, redirect, reverse


# Create your views here.
def index(request):
    page_dict = {'title': 'Triumpvin'}
    return render(request, "index.html", {'topic': 'home', 'theme': 'dark', 'page': page_dict})


def test(request):
    return render(request, "nav.html")


def a(request):
    page_dict = {'title': 'Triumpvin - About Us'}
    return render(request, "about.html", {'page': page_dict})


def contact(request):
    page_dict = {'title': 'Triumpvin - Contact'}
    return render(request, "contact.html", {'page': page_dict})


def about_us(request):
    page_dict = {'title': 'Triumpvin - About Us'}
    return render(request, "about.html", {'page': page_dict})