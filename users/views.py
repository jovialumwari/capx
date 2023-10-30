from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
# TODO pensar nas telas básicas
# TODO criar alguns dados no BD para ter dados para puxar para resultados na tela


def homepage(request):
    context = {}
    return render(request, "users/index.html", context)


@login_required()
def profile(request):
    context = {}
    return render(request, "users/profile.html", context)


def login_oauth(request):
    return redirect(reverse('social:begin', kwargs={"backend": "mediawiki"}))


def logout(request):
    auth_logout(request)
    return redirect(reverse('users:homepage'))
