import zipfile, os, shutil, json

extraction_dir_name = 'Extraction'
zip_file_name = 'zipToExtract.zip'
delimeter = '@@##$$%%^^&&'

def unzip(zip_file):
    deleteArchiveFile()
    open(zip_file_name, 'wb+').write(zip_file)

    deleteExtractionDirectory()
    os.mkdir(extraction_dir_name)

    zip_ref = zipfile.ZipFile(zip_file_name, 'r')
    zip_ref.extractall(extraction_dir_name)
    zip_ref.close()

    data = bytearray()

    for filename in os.listdir(extraction_dir_name):
        data.extend(str.encode(filename))
        data.extend(str.encode(delimeter))
        extracted_file = open(extraction_dir_name + '\\' + filename, 'rb').read()
        if not extracted_file or extracted_file is None:
            return None
        data.extend(extracted_file)

    deleteArchiveFile()
    deleteExtractionDirectory()
    return data

def deleteArchiveFile():
    if os.path.isfile(zip_file_name):
        os.remove(zip_file_name)

def deleteExtractionDirectory():
    if os.path.isdir(extraction_dir_name):
        shutil.rmtree(extraction_dir_name)