install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt

post-install:
	#install textblob dependency
	python -m textblob.download_corpora

format:
	#format the code
	black *.py mylib/*.py

lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py mylib/*.py

test:
	#test
	python -m pytest -vv --cov=mylib/tests --cov=main test_*.py mylib/tests/test_*.py

build: 
	#build container
	docker build -t deploy-fastapi .

run:
	#run docker
	# docker run -p 127.0.0.1:8080:8080 ff737554cc9d

deploy:
	#deploy

all: install post-install lint test deploy
