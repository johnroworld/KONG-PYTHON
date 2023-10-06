FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7 

RUN pip install --upgrade pip

WORKDIR /
ADD . /

CMD ["python3","upload-service.py"]