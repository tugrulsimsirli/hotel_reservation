.PHONY: build up down
build: down up

down:
	@echo "Stopping and removing containers, networks, volumes..."
	docker compose down -v

up:
	@echo "Building and starting containers..."
	docker compose up --build

reqfesh:
	@echo "Packages re-installing..."
	pip install -r requirements.txt
