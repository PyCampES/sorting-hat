FROM python:alpine3.12

WORKDIR /src
COPY requirements.txt /src

RUN pip install -r requirements.txt
ADD . /src

CMD ["PYTHON", "main.py"]
