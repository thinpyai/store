#!/bin/bash

PYTHONPATH=./src
export PYTHONPATH

uvicorn --factory app:main --host 0.0.0.0 --port 8000 --log-config "../conf/logging.yml"
