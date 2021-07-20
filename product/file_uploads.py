from django.core.files.storage import default_storage, FileSystemStorage
from openpyxl import load_workbook
import os, math, csv

def checkIfExist(path):
    return os.path.exists(path)

def createDirectory(path):
    os.mkdir(path)

def saveFileData(path=None, contents=None):
    fs = FileSystemStorage()
    default_storage.save(path, contents)

def processXlsx(file, path, filename):
    wb = load_workbook(file)
    sheetname = "Sheet1"
    ws = wb[sheetname]

    max_content_of_csv = 10
    number_of_chunks = 1 if ws.max_row <= max_content_of_csv else math.ceil(ws.max_row / max_content_of_csv)

    headers=[]
    for cell in ws[1]:
        headers.append(cell.value)

    all_rows = []
    for row in ws.iter_rows(min_row=2):
        all_rows.append(','.join([str(cell.value) for cell in row]))

    # create chunk of csv
    for x in range(number_of_chunks):
        chunk_filename = "{filename}_chunk_{chunk_number}.csv".format(filename=filename, chunk_number=x)
        full_directory = os.path.join(path, chunk_filename)
        with open(full_directory, mode='w', newline='') as csv_writer:
            csv_writer = csv.writer(csv_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            start = x*max_content_of_csv
            end = (x*max_content_of_csv) + max_content_of_csv
            rows_to_insert = all_rows[start:end]
            for i in rows_to_insert:
                csv_writer.writerow(i.split(','))
        

def processCsv(file, path, filename):
    csv_reader = file.read().decode().split("\n")
    total_rows = len(csv_reader) - 1 # headers not included
    all_rows = csv_reader[1:]

    max_content_of_csv = 10
    number_of_chunks = 1 if total_rows <= max_content_of_csv else math.ceil(total_rows / max_content_of_csv)

    # create chunk of csv
    for x in range(number_of_chunks):
        chunk_filename = "{filename}_chunk_{chunk_number}.csv".format(filename=filename, chunk_number=x)
        full_directory = os.path.join(path, chunk_filename)
        with open(full_directory, mode='w', newline='') as csv_writer:
            csv_writer = csv.writer(csv_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            start = x*max_content_of_csv
            end = (x*max_content_of_csv) + max_content_of_csv
            rows_to_insert = all_rows[start:end]
            for i in rows_to_insert:
                csv_writer.writerow([item.rstrip() for item in i.split(',')])
