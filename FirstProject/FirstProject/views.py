from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    # return HttpResponse("Hello ! This is home page")
    return render(request, 'index.html') 

def about_page(request):
    return HttpResponse("Hello ! This is about page")

def contact_page(request):
    return HttpResponse("Hello ! This is contact page")