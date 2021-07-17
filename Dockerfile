FROM python:2.7

WORKDIR /usr/src/app

COPY ./app .

RUN pip install -r requirements.txt

CMD ["test.py"]

ENTRYPOINT ["python"]
