FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/kmnkit/django-pinterest.git

WORKDIR /home/django-pinterest/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-k^m3*6jij)g_7ejix4*2w)b$yq2(rdgkz3%(u7y5ozwa=$!0s%" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]