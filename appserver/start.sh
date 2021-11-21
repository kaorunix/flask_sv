#!/bin/sh

cd ../backend/src
HOSTNAME=$(curl -s http://169.254.169.254/latest/meta-data/public-hostname)
gunicorn main:app -c ../../appserver/gunicorn_settings.py
