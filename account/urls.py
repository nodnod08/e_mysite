from django.urls import include, path
from account import views

urlpatterns = [
    path('', views.index, name='admin-index'),
    path('login/', views.login, name='admin-login'),
]