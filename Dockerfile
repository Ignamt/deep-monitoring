FROM python:3.7.4

COPY . /var/sources/

WORKDIR /var/sources

RUN pip install -U pip setuptools; \
    pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--config", "gunicorn.conf.py", "app:app"]
