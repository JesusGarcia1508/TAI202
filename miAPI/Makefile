.PHONY: help build up down logs clean test install

help:
	@echo "╔════════════════════════════════════════╗"
	@echo "║     Mi API FastAPI - Makefile           ║"
	@echo "╚════════════════════════════════════════╝"
	@echo ""
	@echo "Comandos disponibles:"
	@echo ""
	@echo "  make up          → Inicia los contenedores en background"
	@echo "  make down        → Detiene los contenedores"
	@echo "  make logs        → Ver logs en vivo"
	@echo "  make build       → Construye las imágenes Docker"
	@echo "  make rebuild     → Reconstruye sin caché"
	@echo "  make shell       → Accede a la shell del contenedor"
	@echo "  make psql        → Accede a PostgreSQL"
	@echo "  make clean       → Limpia contenedores y volúmenes"
	@echo "  make test        → Ejecuta tests (próxima feature)"
	@echo "  make install     → Instala dependencias locales"
	@echo ""

up:
	@docker-compose up -d
	@echo "✅ Contenedores iniciados"
	@echo "   - API: http://localhost:5000/docs"
	@echo "   - DB: localhost:5434"

down:
	@docker-compose down
	@echo "✅ Contenedores detenidos"

logs:
	@docker-compose logs -f

build:
	@docker-compose build

rebuild:
	@docker-compose build --no-cache

shell:
	@docker-compose exec api sh

psql:
	@docker-compose exec postgres psql -U admin -d DB_miapi

clean:
	@docker-compose down -v
	@echo " Contenedores y volúmenes eliminados"

test:
	@echo " Tests no configurados aún"

install:
	@echo "Instalando dependencias..."
	@python -m venv venv
	@echo "Entorno virtual creado"
	@echo ""
	@echo "Actívalo con:"
	@echo "  - Windows: venv\Scripts\activate"
	@echo "  - Linux/Mac: source venv/bin/activate"
