from datetime import datetime
from django.shortcuts import redirect

class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

class CustomAuthMiddleware(BaseMiddleware):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.resolver_match.url_name == 'admin-index':
            print("*****************")
            print(request.resolver_match.kwargs)
            print("*****************")
            if not request.user.is_authenticated:
                return redirect('/admin/login')
        return None