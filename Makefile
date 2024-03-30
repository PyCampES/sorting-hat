build:
	docker build -f docker/Dockerfile -t sorting-hat ./src/

install: build
	docker run --name sorting-hat sorting-hat

dev:
	docker compose -f docker/docker-compose.yml up -d