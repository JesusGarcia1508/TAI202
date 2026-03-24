# Mi API de Usuarios 👥

API REST completa para gestionar usuarios, desarrollada con **FastAPI** y **PostgreSQL**, desplegada en **Docker**.

## 📋 Descripción

Sistema de gestión de usuarios con operaciones CRUD completas:
- **C**reate: Crear nuevos usuarios
- **R**ead: Obtener usuarios (todos o por ID)
- **U**pdate: Actualizar usuarios (completo o parcial)
- **D**elete: Eliminar usuarios (requiere autenticación)

## 🚀 Características

✅ API moderna con **FastAPI**  
✅ Base de datos **PostgreSQL**  
✅ Autenticación HTTP Basic  
✅ Documentación interactiva automática (Swagger UI)  
✅ Validación de datos con Pydantic  
✅ Containerizado con Docker  
✅ Soporte CORS habilitado  
✅ Endpoints completamente documentados  

## 📁 Estructura del Proyecto

```
miAPI/
├── app/
│   ├── main.py                 # Aplicación principal FastAPI
│   ├── models/
│   │   └── usuario.py         # Validación de datos (Pydantic)
│   ├── data/
│   │   ├── db.py              # Configuración de base de datos
│   │   ├── usuario.py         # Modelo SQLAlchemy
│   │   └── database.py        # Datos de prueba
│   ├── router/
│   │   ├── usuario.py         # Endpoints CRUD de usuarios
│   │   └── misc.py            # Endpoints de prueba
│   └── security/
│       └── auth.py            # Autenticación HTTP Basic
├── dockerfile                  # Configuración Docker
├── docker-compose.yml          # Orquestación de servicios
├── requirements.txt            # Dependencias Python
├── .env.example                # Variables de entorno (ejemplo)
└── README.md                   # Este archivo
```

## 🛠️ Requisitos

- Docker
- Docker Compose
- Python 3.12+ (para desarrollo local)

## 🐳 Instalación y Ejecución con Docker

### 1. Clonar el proyecto

```bash
git clone <tu-repositorio>
cd miAPI
```

### 2. Ejecutar con Docker Compose

```bash
docker-compose up -d
```

Esto inicia:
- **API FastAPI** en `http://localhost:5000`
- **PostgreSQL** en `localhost:5434`

### 3. Acceder a la documentación interactiva

Abre tu navegador y ve a:

- **Swagger UI** (Interfaz interactiva): http://localhost:5000/docs
- **ReDoc** (Documentación alternativa): http://localhost:5000/redoc
- **OpenAPI JSON**: http://localhost:5000/openapi.json

## 📚 Endpoints Disponibles

### Utilidades (GET)

```
GET /                        # Prueba simple
GET /bienvenido             # Prueba con espera de 5s
GET /v1/parametroOb/{id}    # Parámetro obligatorio
GET /v1/parametroOp/        # Parámetro opcional
```

### Usuarios CRUD

```
GET    /v1/usuarios/        # Obtener todos los usuarios
POST   /v1/usuarios/        # Crear un nuevo usuario
PUT    /v1/usuarios/{id}    # Actualizar usuario (completo)
PATCH  /v1/usuarios/{id}    # Actualizar usuario (parcial)
DELETE /v1/usuarios/{id}    # Eliminar usuario (requiere auth)
```

## 🔐 Autenticación

El endpoint **DELETE** requiere autenticación HTTP Basic:

- **Usuario**: `jesus`
- **Contraseña**: `123456`

En Swagger UI, haz clic en el botón "Authorize" para ingresar las credenciales.

## 📝 Ejemplos de Uso

### Crear un usuario (POST)

```bash
curl -X POST "http://localhost:5000/v1/usuarios/" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 4,
    "nombre": "Juan Pérez",
    "edad": 28
  }'
```

### Obtener todos los usuarios (GET)

```bash
curl "http://localhost:5000/v1/usuarios/"
```

### Actualizar usuario (PUT)

```bash
curl -X PUT "http://localhost:5000/v1/usuarios/1" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "nombre": "Juan García",
    "edad": 29
  }'
```

### Eliminar usuario (DELETE - con autenticación)

```bash
curl -X DELETE "http://localhost:5000/v1/usuarios/1" \
  -u jesus:123456
```

## 💻 Desarrollo Local

### 1. Crear entorno virtual

```bash
python -m venv venv
```

### 2. Activar entorno

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la API

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`

## 🔧 Variables de Entorno

Crear un archivo `.env` (basado en `.env.example`):

```env
DATABASE_URL=postgresql://admin:123456@postgres:5432/DB_miapi
API_PORT=5000
API_HOST=0.0.0.0
AUTH_USERNAME=jesus
AUTH_PASSWORD=123456
DEBUG=True
```

## 🐛 Troubleshooting

### Puerto 5000 ya está en uso

```bash
docker-compose down
```

### Limpiar contenedores y volúmenes

```bash
docker-compose down -v
```

### Ver logs de la aplicación

```bash
docker-compose logs -f api
```

### Ver logs de PostgreSQL

```bash
docker-compose logs -f postgres
```

## 📖 Documentación de FastAPI

FastAPI genera documentación automática basada en:
- Type hints de Python
- Docstrings de las funciones
- Modelos Pydantic
- Configuración de FastAPI

Para aprender más: https://fastapi.tiangolo.com

## 👨‍💻 Autor

**Jesús Manuel García Seijas**

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

¿Preguntas? ¡Abre un issue o contáctame!
