from datetime import datetime
from django.shortcuts import redirect
from django.urls import reverse

class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

class CustomAuthMiddleware(BaseMiddleware):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if '/admin/' in request.path_info and request.resolver_match.url_name != 'admin-login':
            if not request.user.is_authenticated:
                return redirect(reverse('account:admin-login'))
        elif request.resolver_match.url_name == 'admin-login':
            if request.user.is_authenticated:
                if request.user.is_admin:
                    print(reverse('dashboard:admin-dashboard'))
                    return redirect(reverse('dashboard:admin-dashboard'))
                else:
                    return redirect(reverse('account:admin-login'))
        return None