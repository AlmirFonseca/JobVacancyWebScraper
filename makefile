build:
	docker build -t a2-es .

run:
	docker run -p 6080:6080 -p 5900:5900 --name my-running-app a2-es

stop:
	docker stop my-running-app
	docker rm my-running-app

make sequence_run:
	make stop
	make build
	make run

install:
	pip3 install -r requirements.txt

test:
	python3 -m pytest tests --cov=src --cov-report html
