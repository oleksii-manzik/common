FROM python

RUN pip install django requests

COPY . /app

WORKDIR /app

EXPOSE 8000

CMD python manage.py runserver 0:8000
