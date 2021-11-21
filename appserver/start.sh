#!/bin/sh

cd ../backend/src
HOSTNAME=
gunicorn main:app -c ../../appserver/gunicorn_settings.py
