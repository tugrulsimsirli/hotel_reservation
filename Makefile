.PHONY: build down up

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
