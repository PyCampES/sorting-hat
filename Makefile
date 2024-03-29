build:
	docker build -t sorting-hat .

install: build
	docker run --name sorting-hat sorting-hat	