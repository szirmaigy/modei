FROM python:3.6-alpine3.9

COPY ./requirements.txt /modei/requirements.txt

WORKDIR /modei

RUN pip install -r requirements.txt

COPY . /modei

ENTRYPOINT [ "python" ]

EXPOSE  8000
CMD [ "app.py" ]
