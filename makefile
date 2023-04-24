python := python
make := make

#all:
#	$(make) build
#	$(make) upload

build:
	$(python) -m build

upload:
	$(python) -m twine upload ./dist/*
	mv ./dist/* ./dist-history

init:
	$(python) -m pip install -U build
	$(python) -m pip install -U twine
