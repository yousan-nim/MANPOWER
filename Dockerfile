FROM python:3 

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

ENV HOST_MONGODB="mongodb+srv://admin:admin@cluster0.tinickm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000 

WORKDIR /app/server_django

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]