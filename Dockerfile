FROM python:3.11

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

expose 5000

CMD ["python", "server.py"]