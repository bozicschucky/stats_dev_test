FROM python:3.9-alpine

WORKDIR /app

COPY app/ ./app
COPY data.json .
COPY main.py .

# RUN the main function
CMD ["python", "./main.py"]