SRC_DIRS = .

requirements:
	pip install -r requirements.txt

develop: requirements
	pip install -r dev-requirements.txt

quality:
	pep8 $(SRC_DIRS)
	pylint $(SRC_DIRS)

test:
	py.test
