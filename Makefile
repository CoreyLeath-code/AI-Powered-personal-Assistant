# Simplify local development and validation.

install:
	python -m pip install -r requirements.txt -r requirements-dev.txt

install-dashboard:
	python -m pip install -r requirements-dashboard.txt

install-ml:
	python -m pip install -r requirements-ml.txt

run:
	python main.py

test:
	pytest --cov=assistant --cov=modules --cov=agents --cov=scripts --cov-report=term-missing

lint:
	ruff check .

benchmark:
	python benchmarks/assistant_benchmarks.py --output benchmark-results.json
	python -m json.tool benchmark-results.json > /tmp/benchmark-results.pretty.json

docker-build:
	docker build -t ai_personal_assistant .

docker-run:
	docker run -it --env-file .env ai_personal_assistant
