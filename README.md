### Prueba de concepto para reconocimiento de rostro

Esta es una prueba de concepto para hacer una app de reconocimiento de rostro.

## Requerimientos (Linux)

- virtualenv
- librerías: `sudo apt install build-essential cmake pkg-config libx11-dev libatlas-base-dev libgtk-3-dev libboost-python-dev -y`

## Pasos para probar

```
# clonar el repo
git clone git@github.com:fedeotaran/face_rec.git
# entrar al directorio de proyecto
cd face_rec
# crear el entorno virtual
virtualenv -p python3 venv
# instalar las dependencias
pip install -r requirements.txt
# Ejecutar la app
python app.py
```

**Tener en cuenta que el modelo se entrena con una foto de mi rostro y una de
Obama, para que reconozca una cara nueva debe agregarse y encodearse**
