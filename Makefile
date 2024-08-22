PYTHON = python

TESTS_DIR = tests

MAIN_SCRIPT = main.py

help:
	@echo "Available options:"
	@echo "  run   - Run the main application"
	@echo "  test  - Run all tests"
	@echo "  clean - Clean Python cache files"

run:
	$(PYTHON) $(MAIN_SCRIPT)

test:
	$(PYTHON) -m unittest discover $(TESTS_DIR)

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +

.PHONY: help run test clean