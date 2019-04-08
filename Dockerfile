FROM python:latest

COPY ./requirements.txt /app/requirements.txt
COPY app.py textToSpeech.py speechToText.py /app/

WORKDIR /app

ENV FLASK_APP="app.py"

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
