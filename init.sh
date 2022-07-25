#!/bin/bash

set -o errexit
set -o nounset
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python3 manage.py createsuperuser --user admin --noinput --email admin@admin.com --noinput

exec "$@"