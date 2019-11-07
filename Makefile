init:
	python collact/manage.py migrate

test:
	pytest collact/

superuser:
	python collact/manage.py createsuperuser

flush:
	mysql -u root -e 'DROP DATABASE collact; CREATE DATABASE collact CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;'

reset: flush init

run:
	python collact/manage.py runserver

shell:
	python collact/manage.py shell -i bpython

migrate:
	python collact/manage.py makemigrations --merge
	python collact/manage.py makemigrations
	python collact/manage.py migrate

docker_build:
	git rev-parse HEAD > version
	docker build -t collact-server .

docker_login:
	$$(aws ecr get-login --no-include-email)

docker_run: docker_down docker_build
	docker-compose up

docker_down:
	docker-compose down
