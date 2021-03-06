FROM python:3.7

WORKDIR /blog

ENV PYTHONBUFFERED=1 \
    PYTHONPATH=/blog \
    DJANGO_SETTINGS_MODULE=blog.settings \
    PORT=8000 \
    WEB_CURRENCY=3

EXPOSE 8000

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput --clear

CMD gunicorn blog.wsgi:application

