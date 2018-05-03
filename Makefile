shell:
	docker-compose exec web ./manage.py shell_plus --ipython
makemigrations:
	docker-compose exec web ./manage.py makemigrations
showmigrations:
	docker-compose exec web ./manage.py showmigrations
migrate:
	docker-compose exec web ./manage.py migrate
test:
	docker-compose exec web ./manage.py test --settings=config.settings.test --parallel
restart:
	docker-compose restart web
stop:
	docker-compose stop
ps:
	docker-compose ps
logs:
	docker-compose logs
build:
	docker-compose up --build -d
up:
	docker-compose up -d
down:
	docker-compose down -v
bash:
	docker-compose exec web bash
superuser:
	docker-compose exec web ./manage.py createsuperuser
dbshell:
	docker-compose exec web ./manage.py dbshell
