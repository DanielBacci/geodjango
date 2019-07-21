MANAGE_PY=source/manage.py
DEV_SETTINGS=pdv.settings.development
TEST_SETTINGS=pdv.settings.test
VERSION := 1.0.0

set-pythonpath:
	@PYTHONPATH=$(PYTHONPATH):$(shell pwd)/source/

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log

test: clean set-pythonpath
	@py.test -x source/pdv

test-matching: clean set-pythonpath
	@py.test -rxs -k $(Q) --pdb source/pdv

check-security-issues: clean set-pythonpath
	@bandit -r ./source -ll -x 'tests','migrations','features','slack' -c bandit.yaml
	@safety check

coverage: clean set-pythonpath
	@py.test -x --cov source/pdv/ --cov-config=.coveragerc --cov-report=term --cov-report=html --cov-report=xml

requirements-development:
	@pip install -U -r source/requirements/development.txt

runserver-development: clean
	@python $(MANAGE_PY) runserver 0.0.0.0:8000 --settings=$(DEV_SETTINGS)

makemigrations-development:
	@python $(MANAGE_PY) makemigrations $(APP) --settings=$(DEV_SETTINGS)

migrate-dev:
	@python $(MANAGE_PY) migrate --settings=$(DEV_SETTINGS)

test-acceptance:
	behave

flake8:
	@flake8 --show-source .

release-patch:
	bumpversion patch

release-minor:
	bumpversion minor

release-major:
	bumpversion major

check-python-import:
	@cd source/pdv && isort --check-only

fix-python-import:
	@isort -rc -y

lint: clean flake8 check-python-import
