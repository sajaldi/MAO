#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating seed data..."
python manage.py seed_data || true

echo "Starting server..."
exec "$@"
