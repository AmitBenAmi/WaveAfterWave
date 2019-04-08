FROM python:latest

COPY ./requirements.txt /app/requirements.txt
COPY app.py textToSpeech.py speechToText.py /app/

WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT [ "python", "app.py" ]