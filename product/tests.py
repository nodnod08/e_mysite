from django.test import TestCase
from django.conf import settings
from datetime import datetime
from django.core.files.uploadedfile import InMemoryUploadedFile
from product.file_uploads import createChunkCsv, createChunkXlsx
import os, uuid, io

class FileUploadTest(TestCase):
    now = datetime.now()
    pathSample = os.path.join(settings.BASE_DIR, 'public', 'storage', "testFiles")


    # all xlsx config
    filenameSample = "content.xlsx"
    fileSample = os.path.join(settings.BASE_DIR, 'public', 'storage', "testFiles", filenameSample)
    xlsxOnlyfilename = "content"
    # end


    # all csv config
    temp = os.path.join(settings.BASE_DIR, 'public', 'storage', 'temp')
    filenameSampleCSv = "no_content.csv"
    fileSampleCsv = os.path.join(settings.BASE_DIR, 'public', 'storage', "testFiles", filenameSampleCSv)

    actualCsv = open(
        fileSampleCsv, 'rb'
    ).read()

    data = InMemoryUploadedFile(
        file=io.BytesIO(actualCsv),
        field_name='no_content',
        name='{}.csv'.format('no_content'),
        content_type='text/csv',
        size=len(actualCsv),
        charset='utf-8',
    )
    csvOnlyfilename = data.name.split(".")[0]
    new_filename = csvOnlyfilename + "_" + now.strftime("%d-%m-%Y") + "_" +str(uuid.uuid4())

    # end

    fileResult = createChunkXlsx(fileSample, pathSample, xlsxOnlyfilename)
    fileResultCSv = createChunkCsv(data, pathSample, csvOnlyfilename, temp, new_filename)

    # validate no content xlsx
    def testContent(self):
        self.assertDictEqual({"message": "File chunk created", "success": True}, self.fileResult)

    # validate no content csv
    def testContentCsv(self):
        self.assertDictEqual({"message": "File doesn't have a content", "success": False}, self.fileResultCSv)
