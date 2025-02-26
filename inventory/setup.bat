@echo off

REM Instalar dependencias de Python
echo Instalando dependencias de Python...
pip install -r requirements.txt

REM Instalar dependencias de Node.js
echo Instalando dependencias de Node.js...
npm install

REM Compilar el proyecto de Next.js
echo Compilando el proyecto de Next.js...
npm run build

echo Instalación completada. Puedes ejecutar la aplicación con 'npm run dev' para el frontend y 'python api/index.py' para el backend.
pause