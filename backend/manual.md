# server configuration
- Ubuntu
- nginx on host
- docker
- nginx in docker
- postgresql in docker
- .env and .env.db files need to create on host in manage directory
- python 3.11
- Wagtail 6.1.1 (Django framework as dependency)
- gunicorn

## Docker configuration
git pull
docker compose up  --build
docker compose exec scorp python manage.py createsuperuser
docker compose exec scorp python manage.py collectstatic
docker-compose exec scorp python manage.py createsuperuser --settings=app.settings.production
### daemonize

docker-compose up -d --build

### docker commands

sudo docker container ls
sudo docker exec -it 8836acc8f963 /bin/bash
docker-compose down
docker ps --all
docker kill <name>
docker volume prune

## Wagtail/Django commands

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
gunicorn core.wsgi:application -b :8081  --workers=5   --timeout=190 --graceful-timeout=100 --log-level=DEBUG

### virtualenv
apt install python3.11-venv
python3.11 -m venv venv
source ./venv/bin/activatepip  install -r requirements.txt
