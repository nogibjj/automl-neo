install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

format:
	black *.py --line-length 79

lint:
	pylint --disable=R,C,E0401,broad-except,bare-except,consider-using-f-string *.py

test:
	# python -m pytest -vv test_run_auto_train.py

train-ludwig:
	time ludwig train --config config.yaml --dataset data/neo.csv

all: install format lint test