# app/Dockerfile
# Базовый образ с Python 3.13.2
FROM python:3.11.5-slim

# Установка рабочей директории
WORKDIR /fast_app

# Копирование всех файлов проекта внутрь контейнера
COPY . .

# Установка зависимостей
RUN pip install --upgrade pip && pip install -r requirements.txt

# Открытие порта для взаимодействия с контейнером
EXPOSE 8005

# Запуск FastAPI-приложения
CMD ["python", "./main.py"]