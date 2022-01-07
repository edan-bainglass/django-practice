from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'basic_app/index.html', context_dict)


def other(request: HttpRequest) -> HttpResponse:
    return render(request, 'basic_app/other.html')


def relative(request: HttpRequest) -> HttpResponse:
    return render(request, 'basic_app/relative_url_templates.html')
