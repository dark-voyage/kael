from django.shortcuts import redirect


def home(request):
    response = redirect('https://genemator.me/')
    return response
