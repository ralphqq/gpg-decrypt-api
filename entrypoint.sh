#!/bin/bash

set -e

source /home/venv/bin/activate

# Generate secret key for Flask app
echo SECRET_KEY=$(\
python -c"import random; print(''.join(random.SystemRandom().\
choices('abcdefghijklmnopqrstuvwxyz0123456789', k=50)))"\
) >> .env

# Create symlink
ln -s /home/decrypt_msg_api/run_tests.sh /usr/local/bin/run_tests.sh

# Run test if specified
test_script=$1
if [ "$test_script" == "run_tests.sh" ]; then
  source ./run_tests.sh
fi

exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - decryptmessage:app