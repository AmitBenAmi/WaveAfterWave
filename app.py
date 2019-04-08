from flask import Flask, request
from flask_api import status
from speechToText import textFromSpeech
from textToSpeech import speechFromText
from compressionConvert import convertTextToBinary
import json
import os

app = Flask(__name__)

@app.route('/api/stt', methods=['POST'])
def getTextFromSpeech():
    try:
        audio_file_data = request.data

        if not audio_file_data or audio_file_data is None:
            return 'No empty files are allowed to convert to text\n', status.HTTP_400_BAD_REQUEST
        return textFromSpeech(audio_file_data)
    except Exception as ex:
        return str(ex) + '\n', status.HTTP_500_INTERNAL_SERVER_ERROR

@app.route('/api/stc', methods=['POST'])
def getCompressedFromSpeach():
    try:
        audio_file_data = request.data

        if not audio_file_data or audio_file_data is None:
            return 'No empty files are allowed to convert to text\n', status.HTTP_400_BAD_REQUEST
        compressedData = convertTextToBinary(text=textFromSpeech(audio_file_data))
        
        if compressedData is None:
            return 'Error converting the data correctly, one word isn\'t the same as it was recordered\n', status.HTTP_500_INTERNAL_SERVER_ERROR
        return compressedData
    except Exception as ex:
        return str(ex) + '\n', status.HTTP_500_INTERNAL_SERVER_ERROR

@app.route('/api/tts', methods=['POST'])
def getSpeechFromText():
    try:
        text = request.data

        if isinstance(text, bytes):
            text = text.decode('utf-8')

        if not text:
            return 'No empty strings are allowed to convert to speech\n', status.HTTP_400_BAD_REQUEST
        else:
            return speechFromText(text), status.HTTP_200_OK, {'Content-Type': 'audio/wav'}
    except Exception as ex:
        return str(ex) + '\n', status.HTTP_500_INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)