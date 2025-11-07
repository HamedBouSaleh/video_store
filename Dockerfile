FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY video_store12.py/requirements.txt /app/
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY video_store12.py/ /app/
RUN python manage.py collectstatic --noinput || true
EXPOSE 8000
CMD ["gunicorn", "video_store.wsgi:application", "--bind", "0.0.0.0:8000"]
