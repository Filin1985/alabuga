# Проект Сословия

## Данное приложение позволяет создать трехуровневое сословие жителей

### Используемые технологии

- Python (Django)
- HTML
- CSS

### Инструкция по запуску

- Создайте виртуальное окружение
  `python3 -m venv venv`

- Установите все зависимости
  `pip install -r requirements.txt`
  
- Установите django-seed
  `pip install django-seed`

- Войдите в папку проекта 
  `cd estate`

- Наполните базу данных 
  `python manage.py seed citizen --number=500`

- Запустите приложение
  `python manage.py runserver`

### Авторы

Марат Ихсанов
