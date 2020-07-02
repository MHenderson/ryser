doc:
	pdoc --html ryser --html-dir public
	mv public/ryser/index.html public/index.html
	rm -rf public/ryser

install:
	pip install .

dist:
	python3 setup.py sdist bdist_wheel

release:
	python3 -m twine upload dist/*
