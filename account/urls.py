from django.urls import include, path
from account import views

urlpatterns = [
    path('login/', views.index_login),
]