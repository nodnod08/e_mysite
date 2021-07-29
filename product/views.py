# modules
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.conf import settings
from datetime import datetime
# custom builds
from product.models import ProductType, Products
from product.file_uploads import checkIfExist, createDirectory, createChunkCsv, createChunkXlsx, readContents
from .serializers import ProductSerializer
from reusable import MyPaginator

import json, os, uuid, time

def index(request):
    return render(request, 'modules/product/index.jinja')



def import_page(request):
    return render(request, 'modules/product/import/index.jinja')



def list_page(request):
    return render(request, 'modules/product/list/index.jinja')



def getProductTypee(request):
    all_entries = ProductType.objects.all().values()

    response = JsonResponse({
        "result": list(all_entries),
    })
    return response



def saveManually(request):

    item_price = request.POST.get('item_price')
    item_name = request.POST.get('item_name')
    item_type = request.POST.get('item_type')

    file = request.FILES.get("item_file")

    try:
        product_type = ProductType.objects.get(pk=item_type)
        product = Products(product_name=item_name, product_price=item_price, product_type=product_type, product_photo=file)
        product.save()

        success = True
        message = "Item was saved successfuly, you can now manage it"
    except Exception as e:
        success = False
        if hasattr(e, 'message'):
            message = e.message
        else:
            message = "Unable to save this item. Please try again later"

    response = JsonResponse({
        "success": success,
        "message": message
    })
    return response



def saveFile(request):
    now = datetime.now()
    result = True
    message = ""

    file = request.FILES.get("file")
    filename = file.name.split(".")[0]
    extension = file.name.split(".")[1]

    new_filename = filename + "_" + now.strftime("%d-%m-%Y") + "_" +str(uuid.uuid4())
    group_folder = "csv" if extension == "csv" else "xlsx"

    path = os.path.join(settings.BASE_DIR, 'public', 'storage', 'product_files', group_folder, new_filename)
    temp = os.path.join(settings.BASE_DIR, 'public', 'storage', 'temp')
    
    isExist = checkIfExist(path)

    if not isExist:
        try:
            createDirectory(path)
        except FileNotFoundError as err:
            result = False
            message = "Unable to create directory"

            response = JsonResponse({
                "success": result,
                "message": message,
            })

            return response

    if extension == 'xlsx':
        processXl = createChunkXlsx(file, path, filename)
    else:
        processCs = createChunkCsv(file, path, filename, temp, new_filename)

    saveToDatabase(path)

    response = JsonResponse({
        "success": result,
        "message": message,
    })
    
    return response



def saveToDatabase(path):
    list_of_chunks = os.listdir(path)

    readContents(path, list_of_chunks)



def getItemsPaginate(request):
    page = request.POST.get('page') or 1
    limit = request.POST.get('limit') or 10
    print(request.POST.get("page"))
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)

    paginator = MyPaginator(serializer.data, limit)
    paginated = paginator.do_paginate(page)

    response = JsonResponse({"data": paginated})

    return response
