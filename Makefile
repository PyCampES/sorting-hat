build:
	docker build -t sorting-hat -f docker/Dockerfile ./src/

install: build
	docker run --name sorting-hat sorting-hat

up:
	docker compose -f docker/docker-compose.yml up -d

run:
	docker compose -f docker/docker-compose.yml exec sorting-hat python app/main.py