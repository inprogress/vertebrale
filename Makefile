init:
	pip install -r requirements.txt

test:
	nosetests

coverage:
	nosetests --with-coverage --cover-erase --cover-package=vertebrale --cover-inclusive --cover-branches

.PHONY: init test
