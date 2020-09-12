from django.shortcuts import render

def index(request):
    return render(request,'foodiesapp/index.html')

def breakfast(request):
    return render(request, 'foodiesapp/breakfast.html')

def lunch(request):
    return render(request, 'foodiesapp/lunch.html')

def burger(request):
    return render(request, 'foodiesapp/burger.html')

def kolaches(request):
    return render(request, 'foodiesapp/kolaches.html')

def cookies(request):
    return render(request, 'foodiesapp/cookies.html')

def bread(request):
    return render(request, 'foodiesapp/bread.html')

def gelato(request):
    return render(request, 'foodiesapp/gelato.html')

def coffee(request):
    return render(request, 'foodiesapp/coffee.html')
