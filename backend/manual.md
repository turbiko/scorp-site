# server configuration, fixed for project
- Ubuntu
- nginx on host
- docker
- nginx in docker
- postgresql in docker
- .env and .env.db files need to create on host in manage directory
- python 3.11
- Wagtail 6.1.1 (Django framework as dependency)
- gunicorn

### virtualenv python version 3.11 (for example)
apt install python3.11-venv
python3.12 -m venv venv
pip freeze > requirements.txt
source ./venv/bin/activatepip  install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
gunicorn core.wsgi:application -b :8081  --workers=5   --timeout=190 --graceful-timeout=100 --log-level=DEBUG



## Docker configuration

```bash
git pull
docker compose up  --build
docker compose exec scorp python manage.py createsuperuser
docker compose exec scorp python manage.py collectstatic
docker-compose exec scorp python manage.py createsuperuser --settings=app.settings.production
```

### daemonize

```bash
docker-compose up -d --build

docker-compose restart

docker-compose name for service
docker-compose restart <service_name>
```


### docker commands

```bash
sudo docker container ls
sudo docker exec -it 8836acc8f963 /bin/bash
docker-compose down
docker ps --all
docker kill <name>
docker volume prune
```

## Wagtail/Django commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
gunicorn core.wsgi:application -b :8081  --workers=5   --timeout=190 --graceful-timeout=100 --log-level=DEBUG
```

### virtualenv
```bash
apt install python3.12-venv
python3.12 -m venv venv
source ./venv/bin/activate
pip  install -r requirements.txt
```

### pagination
https://learnwagtail.com/tutorials/how-to-paginate-your-wagtail-pages/
https://www.youtube.com/watch?v=NjTF3kfHdm4&ab_channel=HARDCODD ЛУЧШАЯ ПАГИНАЦИЯ


### i18n (translations)

```bash
mkdir -p your_app_name/locale
```

```bash
django-admin makemessages -l uk
django-admin compilemessages
```