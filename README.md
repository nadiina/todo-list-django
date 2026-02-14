# To-Do List API

**Студентка:** Щербина Надія

**Група:** КВ-51мн

**Лабораторна робота:** №1 - Розробка серверної частини Web-додатка

## Опис завдання
Розробити серверну частину Web-додатку для управління списком справ (To-Do List) з використанням Django та Django REST Framework. Додаток повинен підтримувати створення, редагування, видалення та перегляд завдань, а також реєстрацію користувачів.

## Посилання на звіт 
https://docs.google.com/document/d/16yPPVKSbs7w5lMctBZtDBXpKvrG-EGOqfcSWl_vC1DU/edit?usp=sharing

## Технології
* **Python**
* **Django**
* **Django REST Framework**
* **drf-spectacular** (Swagger/Redoc)
* **SQLite**

## Встановлення та запуск

### 1. Клонування репозиторію
```bash
git clone https://github.com/nadiina/todo-list-django.git
cd todo-list-django
```
Створення віртуального середовища:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
Встановлення залежностей:
```bash
pip install -r requirements.txt
```
Міграції бази даних:
```bash
python manage.py migrate
python manage.py createsuperuser
```
Запуск сервера:
```bash
python manage.py runserver
```

