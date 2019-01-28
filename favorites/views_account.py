from django.shortcuts import render, redirect
from .forms import RegistrationForm, AuthForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def registration(request):
    """ Creating user"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            print(password, confirm_password)
            if password != confirm_password:
                error = "Mots de passe différents : merci de saisir le même mot de passe."
            else:
                user = User.objects.create(username=username, email=email, password=password)
                message = "Votre compte vient d'être créer!"
                login(request, user)
    else:
        form = RegistrationForm()

    return render(request, 'favorites/registration.html', locals())


def login_view(request):
    """ log a user in"""
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = authenticate(username=username, password=password)
                if user is None:
                    # Redirect to a success page.
                    user = User.objects.get(username=username, password=password)
                    login(request, user)
            except User.DoesNotExist:
                # Return an 'invalid login' error message.
                error = "Identifiant ou mot de passe incorrect"

    else:
        form = AuthForm()
    return render(request, 'favorites/login.html', locals())


def logout_view(request):
    """ log a user out -> redirect to a success page"""
    logout(request)
    return redirect('index')


def account(request):
    """ personal page of the user """
    return render(request, 'favorites/account.html')
