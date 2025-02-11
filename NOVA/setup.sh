#!/bin/bash
echo "Configurando NOVA..."

# Crear directorios si no existen
mkdir -p static/css static/js static/images templates

echo "Creando entorno virtual..."
python -m venv venv

echo "Activando entorno virtual..."
source venv/Scripts/activate

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Configuración completada! Para iniciar NOVA, ejecuta 'python app.py'" 