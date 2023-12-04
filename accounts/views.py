from django.contrib.auth import logout
from django.shortcuts import redirect, render

def custom_logout(request):
    logout(request)
    return redirect('index')
