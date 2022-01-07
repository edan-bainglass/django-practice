from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.


def index(request):
    return render(request, 'AppTwo/index.html')


def help(request):
    my_dict = {'page_header': "Help Page"}
    return render(request, 'AppTwo/help.html', context=my_dict)


def users(request):
    user_list = User.objects.order_by('last_name')
    users_dict = {'users': user_list}
    return render(request, 'AppTwo/users.html', context=users_dict)
