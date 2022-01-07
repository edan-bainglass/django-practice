from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import UserProfileInfo
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'basic_app/index.html')


@login_required
def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request: HttpRequest) -> HttpResponse:

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user: User = user_form.save()
            user.set_password(user.password)  # hashing password
            user.save()

            profile: UserProfileInfo = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(
        request, 'basic_app/registration.html', {
            'registered': registered,
            'user_form': user_form,
            'profile_form': profile_form,
        })


def user_login(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user: User = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print(f"Username: {username}\npassword: {password}")
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, 'basic_app/login.html')
