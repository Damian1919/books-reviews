.ONESHELL:
SHELL := /bin/bash

deps:
	source .venv/bin/activate
	pip install -r requirements.txt

run:
	source .venv/bin/activate
	python main.py

run_prod:
	source .venv/bin/activate
	gunicorn wsgi:app -b 0.0.0.0:8000

prepare_db:
	source .venv/bin/activate
	python prepare_db.py

lint:
	source .venv/bin/activate
	flake8 main wsgi

test:
	python -m pytest test.py
