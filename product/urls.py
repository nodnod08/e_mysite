from django.urls import path, re_path
from product import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='admin-product'),
    path('import/', views.import_page, name='admin-product-import'),

    # apis
    path('api/get-product-types/', views.getProductTypee),
    path('api/save-product-manually/', views.saveManually),
    path('api/upload-file-product/', views.saveFile),
]