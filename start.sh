#!/usr/bin/env bash

poetry install --no-root

poetry run uvicorn app.main:app --host 0.0.0.0 --port 10000 --app-dir src
