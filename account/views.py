from django.shortcuts import render
from django.http import JsonResponse
from account.BaseBackend import UserBackend
from django.contrib.auth import login as auth_login
import json

# Create your views here.


def login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        password = data.get('password')
        # process logging in
        user = UserBackend.authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            result = True
        else:
            result = False
        response = JsonResponse({
            "success": result,
        })
        return response
    else:
        return render(request, 'modules/account/login.jinja')

def index(request):
    return render(request, 'modules/admin/index.jinja')