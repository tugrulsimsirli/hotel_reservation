.PHONY: build up down migrate create-migration
# Docker-compose down ve build işlemleri için
build: down up

# Docker-compose down -v işlemi
down:
	@echo "Stopping and removing containers, networks, volumes..."
	docker compose down -v

# Docker-compose up --build işlemi
up:
	@echo "Building and starting containers..."
	docker compose up --build

reqfesh:
	@echo "Packages re-installing..."
	pip install -r requirements.txt

migrate:
	alembic upgrade head

create-migration:
	@if [ -z "$(msg)" ]; then \
		echo "Migration message (-msg) is required"; \
		exit 1; \
	else \
		alembic revision --autogenerate -m "$(msg)"; \
	fi

rollback:
	alembic downgrade -1