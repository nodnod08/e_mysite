# modules
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime
# custom builds
from product.models import ProductType, Products
from product.file_uploads import checkIfExist, createDirectory, saveFileData, processXlsx, processCsv

import json, os, uuid

def index(request):
    return render(request, 'modules/product/index.jinja')

def import_page(request):
    return render(request, 'modules/product/import/index.jinja')

def getProductTypee(request):
    all_entries = ProductType.objects.all().values()

    response = JsonResponse({
        "result": list(all_entries),
    })
    return response

def saveManually(request):
    data = json.loads(request.body.decode('utf-8'))

    item_price = data.get('item_price')
    item_name = data.get('item_name')
    item_type = data.get('item_type')

    try:
        product_type = ProductType.objects.get(pk=item_type)
        product = Products(product_name=item_name, product_price=item_price, product_type=product_type)
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
    file = request.FILES.get("file")
    filename = file.name.split(".")[0]
    extension = file.name.split(".")[1]
    now = datetime.now()
    new_filename = filename + "_" + now.strftime("%d-%m-%Y") + "_" +str(uuid.uuid4())
    group_folder = "csv" if extension == "csv" else "xlsx"
    path = os.path.join(settings.BASE_DIR, 'public', 'storage', 'product_files', group_folder, new_filename)

    isExist = checkIfExist(path)
    if not isExist:
        createDirectory(path)

    if extension == 'xlsx':
        processXlsx(file, path, filename)
    else:
        processCsv(file, path, filename)

    response = JsonResponse({
        "success": True,
    })
    return response
