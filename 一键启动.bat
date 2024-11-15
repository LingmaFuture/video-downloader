@echo off

echo Activating virtual environment...
call .venv\Scripts\activate

echo Starting Django server...
start /b python manage.py runserver

timeout /t 3
start http://127.0.0.1:8000/