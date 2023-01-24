# Instrucciones para la instalación y ambientación:
1. Clonar el repositorio

2. Crear su entorno virtual:
   ```bash
   virtualenv .env
   ```

3. Ejecutarlo con:
   ```bash
   source .env/Scripts/activate
   ```

4. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

5. Crear una carpeta para las credenciales al nivel de archivo manage.py):
> IMPORTANTE LLAMAR AL ARCHIVO COMO ".keys"
   ```bash
   touch .keys
   ```

6. Agregar los siguientes parametros y las credenciales de su base de datos:
- SECRET_KEY=
- DEBUG=
- ENGINE=
- NAME=
- USER=
- PASSWORD=
- HOST=
- PORT=

6. Aplicar migraciones:
   ```bash
   py manage.py migrate
   ```

7. Ejecutar el proyecto:
   ```bash
   python manage.py runserver 
    ```