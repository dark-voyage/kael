from django.shortcuts import redirect


def home(request):
    response = redirect('https://genemator.uz/')
    return response


def github(request, gh):
    response = redirect(f"https://github.com/genemators/{gh}")
    return response
