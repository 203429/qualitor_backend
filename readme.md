# Endpoints
> **Documentar las direcciones de las vistas de cada modulo**
https://docs.google.com/document/d/1U8-JUc48rbYFS7Rh8_JmikJSSDd0gZiaQRBrVwf2n6M/edit?usp=sharing

# Instrucciones para la instalación y ambientación:
1. Clonar el repositorio
    ```bash
    git clone https://github.com/203429/qualitor_backend.git
    ```

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

5. Crear una carpeta para las credenciales al nivel de archivo manage.py:
    > **IMPORTANTE LLAMAR AL ARCHIVO COMO ".keys"**
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

8. Si todo salio bien, dirigirse a `localhost:8000/admin` para verificar la instalación.