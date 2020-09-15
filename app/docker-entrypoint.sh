#!/bin/sh

# Collect static files
# echo "Collect static files"
# python3 manage.py collectstatic --noinput

# Apply database migrations
# echo "Apply migrations"
# python3 manage.py makemigrations
# python3 manage.py migrate

# Start server
echo "Starting server"
python src/manage.py runserver323 0.0.0.0:8000
# gunicorn agencycomms.wsgi -b 0.0.0.0:8000 --workers 2 --threads 4 --timeout 240  & celery worker -A agencycomms --loglevel=info
#celery worker -A agencycomms

