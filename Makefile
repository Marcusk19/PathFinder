init:
	pip install -r requirements.txt

test:
	nosetests tests

run:
	python pathfinder/HUD.python
