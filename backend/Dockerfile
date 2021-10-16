FROM python:3.8.5

WORKDIR /backend/foodgram
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY back_static ../var/html/back_static/
COPY . .
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:5000