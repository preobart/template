SHELL := /bin/zsh -eu -o pipefail

ARG := $(word 2, $(MAKECMDGOALS))
SERVICE := app

.PHONY: clean up down restart build logs shell manage migrate \
        makemigrations createsuperuser check test test_reset \
		update_dependencies

clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

up:
	docker compose up --build -d

down:
	docker compose down

restart: down up

logs:
	docker compose logs -f $(ARG)

shell:
	docker compose exec $(ARG) bash

manage:
	docker compose exec $(SERVICE) python manage.py $(ARG)

migrate:
	docker compose exec $(SERVICE) python manage.py migrate $(ARG)

makemigrations:
	docker compose exec $(SERVICE) python manage.py makemigrations

createsuperuser:
	docker compose exec $(SERVICE) python manage.py createsuperuser

check:
	-ruff check .
	-ruff format --check .

lint:
	ruff check . --fix
	ruff format .

test:
	docker compose exec -T $(SERVICE) python manage.py test $(ARG) --parallel --keepdb

test_reset:
	docker compose exec -T $(SERVICE) python manage.py test $(ARG) --parallel

update_dependencies:
	docker compose down
	docker compose up -d --build
