from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        response = JsonResponse({
            "message": "ayos pre"
        })

        return response
    else:
        return render(request, 'modules/account/login.jinja')

def index(request):
    return render(request, 'modules/admin/index.jinja')