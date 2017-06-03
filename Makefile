init:
	pip install -r requirements.txt

migrate:
	alembic upgrade head

test:
	nosetests

coverage:
	nosetests --with-coverage --cover-erase --cover-package=vertebrale --cover-inclusive --cover-branches

.PHONY: init migrate test
