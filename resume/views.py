from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def portfolio(request):
    return render(request, 'portfolio.html')


def home(request):
    return render(request, 'index.html', context={
        "first_name": "Shushanik",
        "last_name": "Manukyan",
    })
