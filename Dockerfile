FROM python:3.7

WORKDIR /blog

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD py manage.py runserver

