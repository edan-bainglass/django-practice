from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'basic_app/index.html')


def other(request: HttpRequest) -> HttpResponse:
    return render(request, 'basic_app/other.html')


def relative(request: HttpRequest) -> HttpResponse:
    return render(request, 'basic_app/relative_url_templates.html')
