FROM python:2.7-alpine
COPY . /app
COPY data /data
COPY tests/functional/data /test-data
WORKDIR /app
RUN pip install -r requirements.txt