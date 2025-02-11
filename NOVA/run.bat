@echo off
echo Iniciando NOVA...

if not exist venv (
    echo Error: Entorno virtual no encontrado.
    echo Por favor, ejecuta setup.bat primero.
    pause
    exit
)

call venv\Scripts\activate
python app.py