# Actividad-API-sencilla-de-Login-con-FastAPI
Implementar una API REST mínima con FastAPI que permita realizar el proceso de login contra una base de datos embebida (db "quemada" en código) usando sqlmodel. El objetivo es comprender la estructura básica de una API de autenticación (sin complejidades como tokens obligatorios).



1. Activar el entorno virtual: `.\venv\Scripts\activate`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Iniciar el servidor: `uvicorn main:app --reload`


Entrar a `http://127.0.0.1:8000/docs` para realizar pruebas con los usuarios quemados (admin, user, guest).
