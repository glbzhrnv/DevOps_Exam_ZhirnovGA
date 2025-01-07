# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install flake8

# Открываем порт
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]
