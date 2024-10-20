#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    echo "HOST: "$SQL_HOST $SQL_PORT

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
echo "Production environment started...."

# Django management commands
python manage.py makemigrations --settings=core.settings.production
python manage.py migrate --settings=core.settings.production

# Collect static files
python manage.py collectstatic --settings=core.settings.production --no-input --clear

# Compile translation files from .po to .mo
python manage.py compilemessages --settings=core.settings.production

# Update search index (if applicable)
python manage.py update_index --settings=core.settings.production

# Start Gunicorn server
gunicorn core.wsgi:application -b :8000 --workers=5 --timeout=190 --graceful-timeout=100 --log-level=info
exec "$@"