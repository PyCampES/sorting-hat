from python:3.8
copy . /app
workdir /app
run pip install -r requirements.txt
cmd ["python", "app.py"]