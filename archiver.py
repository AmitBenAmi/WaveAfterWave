import zipfile, os, shutil

extraction_dir_name = 'Extraction'
zip_file_name = 'zipToExtract.zip'

def unzip(zip_file):
    deleteArchiveFile()
    open(zip_file_name, 'wb+').write(zip_file)

    deleteExtractionDirectory()
    os.mkdir(extraction_dir_name)

    zip_ref = zipfile.ZipFile(zip_file_name, 'r')
    zip_ref.extractall(extraction_dir_name)
    zip_ref.close()

    extracted_file = None

    for filename in os.listdir(extraction_dir_name):
        extracted_file = open(extraction_dir_name + '\\' + filename, 'rb').read()

    deleteArchiveFile()
    deleteExtractionDirectory()

    return extracted_file

def deleteArchiveFile():
    if os.path.isfile(zip_file_name):
        os.remove(zip_file_name)

def deleteExtractionDirectory():
    if os.path.isdir(extraction_dir_name):
        shutil.rmtree(extraction_dir_name)