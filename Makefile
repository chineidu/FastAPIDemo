.PHONY: setup-venv setup clean-pyc clean-test test mypy lint check

setup-venv:
	python3 -m venv .venv && . .venv/bin/activate
	pip install --upgrade pip
	pip install -r test_requirements.txt

setup:  # fastapi_app is the tag
	DOCKER_BUILDKIT=1 docker build -t fastapi_app -f Dockerfile .

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*
	find . -name '.pytest_cache' -exec rm -fr {} +

clean: clean-pyc clean-test
	find . -name '.my_cache' -exec rm -fr {} +
	rm -rf logs/

test: clean # src is the source code
	. .venv/bin/activate && py.test tests --cov=src --cov-report=term-missing --cov-fail-under 80

mypy:
	. .venv/bin/activate && mypy src

lint:
	. .venv/bin/activate && black src && isort src

checks: test lint mypy clean

run-checks:
	# Use the current working directory as the docker's volume. 
	docker run --rm -it --name run-checks -v $(shell pwd):/opt -t fastapi_app make checks

bash:
	docker run --rm -it --name run-checks -v $(shell pwd):/opt -t fastapi_app bash