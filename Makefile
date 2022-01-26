SHELL=/bin/bash
PATH := .venv/bin:$(PATH)

run:
	@python main.py

install:
	@( \
		if [ ! -d .venv ] ; then python3 -m venv --copies .venv; fi; \
		source .venv/bin/activate; \
		pip install -qU pip; \
		pip install -r requirements.txt; \
		pip install pre-commit; \
		pre-commit install; \
	);
