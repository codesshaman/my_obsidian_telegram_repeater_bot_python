FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY app/requirements.txt .

RUN pip3 install --upgrade pip -r requirements.txt

COPY app .

EXPOSE 8080

CMD ["python3", "/app/main.py"]