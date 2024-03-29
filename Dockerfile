from python:3.10.12
copy . /app
workdir /app
run pip install -r requirements.txt
cmd ["python", "main.py"]