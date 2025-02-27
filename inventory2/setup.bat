@echo off
echo Instalando dependencias...

REM Crear un entorno virtual
python -m venv venv

REM Activar el entorno virtual
call venv\Scripts\activate

REM Instalar las dependencias
pip install -r requirements.txt

echo Dependencias instaladas exitosamente.