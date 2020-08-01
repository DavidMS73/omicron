# Omicron Back
Este proyecto contiene los archivos del backend para el sistema Omicron, proyecto propuesto para la Hackathon Uniandes 2020 (https://hackathon-uniandes-2020.devpost.com/).

# Instrucciones de instalación
1. Tener python 3 instalado.
2. Clonar el repositorio.

**Ubicado en la carpeta del repositorio:**

3. Instalar los requerimientos con:
```
   pip install -r requeriments.txt
```
4. Ejecutar:
```
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py runserver
```
5. En este momento el servidor backend de Omicron debe estar corriendo.

# Agregar datos al servidor
1. Tener el servidor corriendo
2. Entrar a http://localhost:8000
3. Escoger el modelo que se quiere agregar
4. En la última parte de la página llenar el formulario
5. Enviar
