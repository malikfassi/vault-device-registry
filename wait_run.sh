#!/usr/bin/env bash

echo "Waiting for postgres..."

while ! nc -z vault-device-registry-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

./run.sh
