from django import template

register = template.Library()


@register.filter
def app_icon(app_label: str) -> str:

    match app_label:
        case 'auth':
            return 'admin/img/menu/auth.svg'
        
        case _:
            return 'admin/img/menu/app.svg'
