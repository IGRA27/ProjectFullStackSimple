# Simple Full Stack Flask & MongoDB Application

Este proyecto es una aplicación full stack simple que utiliza Flask como backend y MongoDB como base de datos. La interfaz de usuario es servida usando HTML estático. Todo el entorno está dockerizado para facilitar el despliegue y la gestión de dependencias.

## Componentes

- **Flask**: Un micro framework web escrito en Python que se usa para el backend.
- **MongoDB**: Una base de datos NoSQL que almacena los datos de la aplicación.
- **Docker**: Utilizado para crear contenedores que encapsulan los componentes de la aplicación.
- **Docker Compose**: Utilizado para definir y ejecutar aplicaciones Docker multi-contenedor.

## Estructura del proyecto

```plaintext
ProjectFullStackSimple/
|-- backend/
|   |-- Dockerfile
|   |-- app.py
|   |-- requirements.txt
|-- frontend/
|   |-- Dockerfile
|   |-- index.html
|-- docker-compose.yml




Configuración
Requisitos
Docker Desktop
Docker Compose

docker-compose up --build
