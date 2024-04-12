FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt .
COPY server.py .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "./server.py"]