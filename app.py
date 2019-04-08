from flask import Flask, request
from flask_api import status
from speechToText import textFromSpeech
from textToSpeech import speechFromText
from compressionConvert import convertTextToBinary
from archiver import unzip, zip
import json
import os

app = Flask(__name__)

@app.route('/api/stt', methods=['POST'])
def getTextFromSpeech():
    try:
        audio_file_data = request.data

        if not audio_file_data or audio_file_data is None:
            return 'Empty files aren\'t allowed to convert to text\n', status.HTTP_400_BAD_REQUEST
        return textFromSpeech(audio_file_data)
    except Exception as ex:
        return str(ex) + '\n', status.HTTP_500_INTERNAL_SERVER_ERROR

@app.route('/api/stc', methods=['POST'])
def getCompressedFromSpeach():
    try:
        audio_file_data = request.data

        if not audio_file_data or audio_file_data is None:
            return 'Empty files aren\'t allowed to convert to text\n', status.HTTP_400_BAD_REQUEST
        compressedData = convertTextToBinary(text=textFromSpeech(audio_file_data))
        
        if compressedData is None:
            return 'Error converting the data correctly, one word isn\'t the same as it was recordered\n', status.HTTP_500_INTERNAL_SERVER_ERROR
        return compressedData
    except Exception as ex:
        return str(ex) + '\n', status.HTTP_500_INTERNAL_SERVER_ERROR

@app.route('/api/yr', methods=['POST'])
def getCompressedFromSpeach():
    try:
        audio_file_data = request.data

        if not audio_file_data or audio_file_data is None:
            return 'Empty files aren\'t allowed to convert to text\n', status.HTTP_400_BAD_REQUEST
        compressedData = convertTextToBinary(text=textFromSpeech(audio_file_data))
        
        if compressedData is None:
            return 'Error converting the data correctly, one word isn\'t the same as it was recordered\n', status.HTTP_500_INTERNAL_SERVER_ERROR
        #return compressedData
        return open('nature.7z', 'rb').read()
    except Exception as ex:
        return str(ex) + '\n', status.HTTP_500_INTERNAL_SERVER_ERROR

@app.route('/api/tts', methods=['POST'])
def getSpeechFromText():
    try:
        text = request.data

        if isinstance(text, bytes):
            text = text.decode('utf-8')

        if not text:
            return 'Empty strings aren\'t allowed to convert to speech\n', status.HTTP_400_BAD_REQUEST
        else:
            return speechFromText(text), status.HTTP_200_OK, {'Content-Type': 'audio/wav'}
    except Exception as ex:
        return str(ex) + '\n', status.HTTP_500_INTERNAL_SERVER_ERROR

@app.route('/api/ffa', methods=['POST'])
def getFileFromArchive():
    try:
        archive_file = request.data

        if not archive_file or archive_file is None:
            return 'Empty files aren\'t allowed to unarchive\n', status.HTTP_400_BAD_REQUEST
        data = unzip(archive_file)
        if data is None:
            return 'Error handling the archive', status.HTTP_400_BAD_REQUEST
        return data
    except Exception as ex:
        return str(ex) + '\n', status.HTTP_500_INTERNAL_SERVER_ERROR

@app.route('/api/aff', methods=['POST'])
def getArchiveFromFile():
    try:
        file_to_archive = request.data

        if not file_to_archive or file_to_archive is None:
            return 'Empty files aren\'t allowed to archive\n', status.HTTP_400_BAD_REQUEST
        data = zip(file_to_archive)
        if data is None:
            return 'Error handling the archive', status.HTTP_400_BAD_REQUEST
        return data
    except Exception as ex:
        return str(ex) + '\n', status.HTTP_500_INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)