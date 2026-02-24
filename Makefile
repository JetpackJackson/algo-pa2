all:
	./.venv/bin/python src/main.py

init:
	python -m venv .venv
	./.venv/bin/pip install -r requirements.txt
