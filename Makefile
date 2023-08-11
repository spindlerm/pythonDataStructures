
test:
	python -m pytest tests/*.py
format:
	black .
lint:
	pylint *.py tests/ --disable=E Makefile

all: format lint test



