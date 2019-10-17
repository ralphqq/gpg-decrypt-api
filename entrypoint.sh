#!/bin/bash

set -e

source /home/venv/bin/activate

echo Generating secret key for Flask app
echo SECRET_KEY=$(\
python -c"import random; print(''.join(random.SystemRandom().\
choices('abcdefghijklmnopqrstuvwxyz0123456789', k=50)))"\
) >> .env

/bin/bash