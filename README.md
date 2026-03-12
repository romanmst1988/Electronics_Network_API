
# Electronics Network API

REST API для управления сетью по продаже электроники.

Проект реализует иерархическую модель сети поставщиков (завод → розничная сеть → предприниматель) 
с возможностью управления звеньями сети, продуктами и задолженностями.

Проект разработан на **Django + Django REST Framework** с использованием **PostgreSQL** и **Docker**.

---

# Функциональность

## Управление сетью поставщиков
- создание звена сети
- редактирование данных
- удаление
- просмотр списка
- фильтрация по стране

## Иерархия сети

Каждое звено сети может иметь поставщика.

Уровни сети формируются автоматически:

- Завод → уровень 0  
- Розничная сеть → уровень 1  
- ИП → уровень 2  

## Управление продуктами

Каждый продукт содержит:

- название
- модель
- дату выхода на рынок
- привязку к звену сети

## Задолженность

У каждого звена сети есть поле:

`debt`

Задолженность **нельзя изменять через API**.

## Административная панель

В Django Admin реализовано:

- ссылка на поставщика
- фильтр по городу
- поиск
- admin action для очистки задолженности

## Безопасность

Доступ к API имеют только пользователи:

- `is_active = True`
- `is_staff = True`

## Аутентификация

Используется JWT (JSON Web Token)

---

# Стек технологий

- Python 3.11
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Docker Compose
- pytest
- factory-boy
- drf-spectacular (Swagger)

---

# Архитектура проекта

- backend
- │
- ├── config
- │ ├── settings.py
- │ ├── urls.py
- │
- ├── network
- │ ├── models.py
- │ ├── serializers.py
- │ ├── views.py
- │ ├── admin.py
- │ ├── tests
- │
- ├── products
- │ ├── models.py
- │ ├── admin.py
- │ ├── tests
- │
- ├── users
- │ ├── permissions.py
- │ ├── tests
- │
- └── tests
- └── factories.py

---

# Установка и запуск

## 1. Клонировать репозиторий

git clone https://github.com/romanmst1988/Electronics_Network_API.git
cd Electronics_Network_API

---

## 2. Создать `.env`

Создать файл:

backend/.env

Пример:

POSTGRES_DB=electronics_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

---

## 3. Запуск проекта

docker compose up --build

После запуска API доступно:

http://localhost:8000

---

# Миграции

docker compose exec web python backend/manage.py makemigrations
docker compose exec web python backend/manage.py migrate

---

# Создание суперпользователя

docker compose exec web python backend/manage.py createsuperuser

Админ панель:

http://localhost:8000/admin

---

# Документация API

Swagger доступен по адресу:

http://localhost:8000/api/docs/

---

# JWT авторизация

Получить токен:

POST /api/token/

Пример запроса:

{
  "username": "admin",
  "password": "password"
}

Ответ:

{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}

---

# Основные эндпоинты

## Сеть поставщиков

GET /api/network/  
POST /api/network/  
GET /api/network/{id}/  
PATCH /api/network/{id}/  
DELETE /api/network/{id}/  

Фильтрация по стране:

/api/network/?country=USA

---

# Тестирование

В проекте используется:

- pytest
- pytest-django
- factory-boy
- pytest-cov

Запуск тестов:

docker compose exec web pytest backend --cov

Результат покрытия:

18 tests  
99% coverage

---

# Особенности реализации

- иерархическая модель сети
- вычисление уровня сети
- запрет изменения задолженности через API
- фильтрация через DjangoFilterBackend
- права доступа через кастомные permissions
- admin action очистки долга
- Swagger документация
- тесты на модели, API, permissions и admin

---

# Автор

Roman MST

GitHub:
https://github.com/romanmst1988
