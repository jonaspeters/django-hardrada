from django.http import HttpRequest


def actions(request: HttpRequest) -> dict:

    return {
        'menu': request.session.get('menu', 'extended'),
        'theme': request.session.get('theme', 'dark'),
    }
