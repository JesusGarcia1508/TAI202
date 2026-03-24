@echo off
REM Script para iniciar la API FastAPI con Docker

ECHO.
ECHO ========================================
ECHO  Mi API FastAPI con Docker
ECHO ========================================
ECHO.

REM Verificar si Docker está instalado
docker --version >nul 2>&1
if errorlevel 1 (
    ECHO ERROR: Docker no está instalado o no está en el PATH
    ECHO Por favor instala Docker Desktop desde https://www.docker.com/products/docker-desktop
    PAUSE
    EXIT /B 1
)

ECHO [1] Iniciando servicios...
docker-compose up -d

ECHO.
ECHO [2] Esperando a que los servicios estén listos...
timeout /t 5 /nobreak

ECHO.
ECHO ========================================
ECHO  ✅ Servicios Iniciados
ECHO ========================================
ECHO.
ECHO Tu API está disponible en:
ECHO   - API Base: http://localhost:5000
ECHO   - Swagger UI: http://localhost:5000/docs
ECHO   - ReDoc: http://localhost:5000/redoc
ECHO.
ECHO PostgreSQL está en: localhost:5434
ECHO Credenciales: admin / 123456
ECHO.
ECHO Para ver los logs:
ECHO   docker-compose logs -f
ECHO.
ECHO Para detener los servicios:
ECHO   docker-compose down
ECHO.
ECHO ========================================
PAUSE
