#!/bin/bash

set -e

source /home/venv/bin/activate

echo Generating secret key for Flask app
echo SECRET_KEY=$(\
python -c"import random; print(''.join(random.SystemRandom().\
choices('abcdefghijklmnopqrstuvwxyz0123456789', k=50)))"\
) >> .env

echo Creating symlink
ln -s /home/decrypt_msg_api/run_tests.sh /usr/local/bin/run_tests.sh

echo Starting up gunicorn
exec gunicorn -b 0.0.0.0:80 --access-logfile - --error-logfile - decryptmessage:app