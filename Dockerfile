FROM python:latest

COPY ./requirements.txt /app/requirements.txt
COPY ./*.py /app/*.py

WORKDIR /app

ENV FLASK_APP="app.py"

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask" ]

CMD [ "run" ]
