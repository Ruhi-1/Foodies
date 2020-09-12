from django.shortcuts import render

def index(request):
    return render(request,'foodiesapp/index.html')

def breakfast(request):
    return render(request, 'foodiesapp/breakfast.html')

def lunch(request):
    return render(request, 'foodiesapp/lunch.html')
