#!/bin/bash

# Script para iniciar la API FastAPI con Docker

echo ""
echo "========================================"
echo "  Mi API FastAPI con Docker"
echo "========================================"
echo ""

# Verificar si Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker no está instalado"
    echo "Por favor instala Docker desde https://www.docker.com/products/docker-desktop"
    exit 1
fi

echo "[1] Iniciando servicios..."
docker-compose up -d

echo ""
echo "[2] Esperando a que los servicios estén listos..."
sleep 5

echo ""
echo "========================================"
echo "  ✅ Servicios Iniciados"
echo "========================================"
echo ""
echo "Tu API está disponible en:"
echo "   - API Base: http://localhost:5000"
echo "   - Swagger UI: http://localhost:5000/docs"
echo "   - ReDoc: http://localhost:5000/redoc"
echo ""
echo "PostgreSQL está en: localhost:5434"
echo "Credenciales: admin / 123456"
echo ""
echo "Para ver los logs:"
echo "   docker-compose logs -f"
echo ""
echo "Para detener los servicios:"
echo "   docker-compose down"
echo ""
echo "========================================"
