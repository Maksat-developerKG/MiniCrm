## Установка

1. Склонируйте проект:

```bash
git clone git@github.com:Maksat-developerKG/minicrm.git
cd yourproject

Создайте виртуальное окружение:
python -m venv venv
source venv/bin/activate  # на Windows: venv\Scripts\activate


Установите зависимости:
pip install -r requirements.txt


Создайте .env файл на основе .env.example:
cp .env.example .env



Настройте .env под себя и запустите сервер:
python manage.py migrate
python manage.py runserver





---

## Шаг 5: Пример `.env.example`

env
DEBUG=True
SECRET_KEY=change-me
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432
