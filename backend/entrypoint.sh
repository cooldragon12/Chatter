#!/bin/bash

echo "Starting entrypoint.sh"
echo "Applying migrations"

python manage.py migrate

exec "$@"
