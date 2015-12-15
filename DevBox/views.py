from django.shortcuts import render

def home_page(request):
    return render(request,'home_page.html')

def get_started(request):
    return render(request,'get_started.html')
