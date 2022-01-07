from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from AppTwo.models import User
from AppTwo.forms import UserForm

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'AppTwo/index.html')


def help(request: HttpRequest) -> HttpResponse:
    my_dict = {'page_header': "Help Page"}
    return render(request, 'AppTwo/help.html', context=my_dict)


def users(request: HttpRequest) -> HttpResponse:
    user_list = User.objects.order_by('last_name')
    users_dict = {'users': user_list}
    return render(request, 'AppTwo/users.html', context=users_dict)


def new_users(request: HttpRequest) -> HttpResponse:
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)  # back to homepage
        else:
            print("ERROR FORM INVALID")

    return render(request, 'AppTwo/new_users.html', context={'form': form})
