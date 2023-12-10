build:
	docker build --platform linux/x86_64 -t a2-es .

run:
	docker run  \
	--rm -p 5900:5900 \
	--name my-running-app a2-es

stop:
	docker stop my-running-app
	docker rm my-running-app

make sequence_run:
	make stop
	# make build
	# make run
	docker build -t a2-es .
	docker run -p 6080:6080 -p 5900:5900 --name my-running-app a2-es
