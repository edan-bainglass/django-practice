from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import forms

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'basicapp/index.html')


def form_name_view(request: HttpRequest) -> HttpResponse:
    form = forms.Form()

    if request.method == 'POST':
        form = forms.Form(request.POST)

        if form.is_valid():
            print("Validation passed.")
            print("NAME:", form.cleaned_data['name'])
            print("EMAIL:", form.cleaned_data['email'])
            print("TEXT:", form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', context={'form': form})
