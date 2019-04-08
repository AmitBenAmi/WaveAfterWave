FROM python:latest

COPY ./requirements.txt /app/requirements.txt
COPY app.py textToSpeech.py speechToText.py compressionConvert.py word_to_bytes.json archiver.py nature.7z /app/

WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 443

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]