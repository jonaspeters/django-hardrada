from django.http import HttpRequest
from django.contrib import messages


def actions(request: HttpRequest) -> dict:

    return {
        'menu': request.session.get('menu', 'extended'),
        'theme': request.session.get('theme', 'dark'),
    }
