#!/bin/sh

alembic upgrade head
fastapi run main.py --port 80
