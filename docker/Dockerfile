FROM python:alpine3.18

WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt
ADD . /src

CMD ["PYTHON", "main.py"]
