# modules
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.conf import settings
from datetime import datetime
from django.db.models import Q, Case, Value, When
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
    data = json.loads(request.body.decode('utf-8'))

    page = data.get('page') or 1
    limit = data.get('limit') or 10
    filters = data.get('filters')

    products = Products.objects

    where_clause = []

    if filters['name']:
        where_clause.append("product_name LIKE '%%{0}%%'".format(filters['name']))
    
    if filters['item_type']:
        where_clause.append("""
            product_type_id IN (SELECT id FROM product_types where id = {0})
        """.format(filters['item_type']))

    if filters['min_price'] and filters['max_price']:
        min_price = "{:.2f}".format(float(filters['min_price']))
        max_price = "{:.2f}".format(float(filters['max_price']))

        where_clause.append("""
            product_price BETWEEN {0} AND {1}
        """.format(min_price, max_price))

    if len(where_clause):
        where_clause = " WHERE " + (" OR ".join(where_clause))
    else:
        where_clause = ""
    products = products.raw("SELECT * FROM products" + where_clause)

    serializer = ProductSerializer(products, many=True)

    paginator = MyPaginator(serializer.data, limit)
    paginated = paginator.do_paginate(page)

    response = JsonResponse({"data": paginated})

    return response

def updateItem(request):
    data = json.loads(request.body.decode('utf-8'))
    result = True
    message = ""
    
    type = ProductType.objects.get(pk = data['product_type']['id'])
    product = Products.objects.get(pk = data['id'])

    product.product_type = type
    product.product_name = data['product_name']
    product.product_price = "{:.2f}".format(float(data['product_price']))
    product.quantity = int(data['quantity'])
    product.save()
    
    response = JsonResponse({
        "success": result,
        "message": message,
    })
    
    return response