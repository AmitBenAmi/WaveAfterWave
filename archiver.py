import zipfile, os, shutil, json

extraction_dir_name = 'Extraction'
extract_zip_file_name = 'zipToExtract.zip'
archive_zip_file_name = 'zipToArchive.zip'
file_name_to_archive = 'file_to_archive'
delimeter = '@@##$$%%^^&&'

def unzip(zip_file):
    deleteFile(extract_zip_file_name)
    open(extract_zip_file_name, 'wb+').write(zip_file)

    deleteExtractionDirectory()
    os.mkdir(extraction_dir_name)

    zip_ref = zipfile.ZipFile(extract_zip_file_name, 'r')
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

    deleteFile(extract_zip_file_name)
    deleteExtractionDirectory()
    return data

def deleteFile(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)

def deleteExtractionDirectory():
    if os.path.isdir(extraction_dir_name):
        shutil.rmtree(extraction_dir_name)

def zip(file_to_archive):
    open(file_name_to_archive, 'wb+').write(file_to_archive)
    zout = zipfile.ZipFile(archive_zip_file_name, 'w', zipfile.ZIP_DEFLATED)
    zout.write(file_name_to_archive)
    zout.close()
    zip_data = open(archive_zip_file_name, 'rb').read()
    deleteFile(archive_zip_file_name)
    deleteFile(file_name_to_archive)

    return zip_data