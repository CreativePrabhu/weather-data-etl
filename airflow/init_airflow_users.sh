#!/bin/bash

# Wait for Airflow to be ready
echo "Waiting for Airflow to be ready..."
sleep 20  # Adjust the sleep time if needed

# Create Airflow user
airflow users create \
  --username admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com \
  --password admin

# Call the default entrypoint of Airflow
exec "$@"
