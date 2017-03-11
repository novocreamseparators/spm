from django.shortcuts import render


def Home(request):
    return render(request, 'Home/main.html')


def about(request):
    return render(request, 'Home/about.html')
