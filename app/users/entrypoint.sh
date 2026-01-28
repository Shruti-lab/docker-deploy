#!/bin/bash

sleep 10

echo "⏳ Waiting for PostgreSQL..."

while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL is connected - User Service"


echo "Starting Gunicorn..."
exec gunicorn --bind  0.0.0.0:5002  run:app

tail -f /dev/null