from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@login_required
def hardrada_actions(request: HttpRequest, action: str) -> HttpResponse:
    """View for set menu state in session"""


    match action:
        case 'menu':
            menu = request.POST.get('extended', 'true')
            request.session['menu'] = 'extended' if menu == 'true' else 'collapsed'
            return JsonResponse({
                'message': 'Menu state update',
            })

        case 'theme':
            theme = request.POST.get('theme')
            request.session['theme'] = 'light' if theme == 'dark' else 'dark'
            return JsonResponse({
                'message': 'Menu state update',
            })
        
        case _:
            raise Exception(f'')
