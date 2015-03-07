from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def login_redirect(request):
    """Redirige de /accounts/login a /login."""
    return HttpResponseRedirect('/login')