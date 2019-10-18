#!/bin/bash

set -e

source /home/venv/bin/activate

echo Generating secret key for Flask app
echo SECRET_KEY=$(\
python -c"import random; print(''.join(random.SystemRandom().\
choices('abcdefghijklmnopqrstuvwxyz0123456789', k=50)))"\
) >> .env

echo Starting up gunicorn
exec gunicorn -b 0.0.0.0:80 --access-logfile - --error-logfile - decryptmessage:app