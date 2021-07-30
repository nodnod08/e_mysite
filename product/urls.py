from django.urls import path, re_path
from product import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='admin-product'),
    path('import/', views.import_page, name='admin-product-import'),
    path('list/', views.list_page, name='admin-product-list'),

    # apis
    path('api/get-product-types/', views.getProductTypee),
    path('api/get-items-paginate', views.getItemsPaginate),
    path('api/save-product-manually/', views.saveManually),
    path('api/update-product/', views.updateItem),
    path('api/upload-file-product/', views.saveFile),
]