#!/bin/bash

if [[ "$1" == "celery" ]]; then
    echo "Starting celery worker..."
    celery --app=src.tasks.tasks:celery worker -l INFO
elif [[ "$1" == "flower" ]]; then
    echo "Starting celery flower..."
    celery --app=src.tasks.tasks:celery flower
 fi
