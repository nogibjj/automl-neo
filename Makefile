install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

format:
	black *.py --line-length 79

lint:
	pylint --disable=R,C,E0401,broad-except,bare-except,consider-using-f-string *.py

train-ludwig:
	time ludwig train --config config.yaml --dataset data/neo.csv

test:
	pytest test_data_deepchecks.py

hyperopt-ludwig:
	time ludwig hyperopt --config config.yaml --dataset data/neo.csv

all: install format lint test