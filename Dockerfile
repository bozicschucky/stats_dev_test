FROM python:3.9-alpine

WORKDIR /app

COPY main.py .

# RUN pip install some packages ...

CMD ["python", "./main.py"]