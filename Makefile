build:
	docker build -t sorting-hat -f docker/Dockerfile ./src/

install: build
	docker run --name sorting-hat sorting-hat

dev:
	docker compose -f docker/docker-compose.yml up -d