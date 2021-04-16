FROM python:3.7

WORKDIR /blog

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD gunicorn blog.wsgi:application --bind 0.0.0.0:8000