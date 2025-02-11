@echo off
echo Configurando NOVA...

REM Crear directorios si no existen
mkdir static 2>nul
mkdir static\css 2>nul
mkdir static\js 2>nul
mkdir static\images 2>nul
mkdir templates 2>nul

echo Creando entorno virtual...
python -m venv venv

echo Activando entorno virtual...
call venv\Scripts\activate

echo Instalando dependencias...
pip install -r requirements.txt
pip install SpeechRecognition
pip install PyAudio
pip install pyttsx3

echo Configuración completada! Para iniciar NOVA, ejecuta 'run.bat'
pause