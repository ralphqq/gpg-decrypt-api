FROM python:3.7-slim-buster
LABEL maintainer="ralph.quirequire@gmail.com"

# Install gpg
RUN apt-get update && apt-get install -y gnupg

# Set working directory
WORKDIR /home/decrypt_msg_api

# Create a virtual environment
RUN python -m venv /home/venv

# Install dependencies and gunicorn app server
COPY requirements.txt .
RUN /home/venv/bin/pip install -r requirements.txt
RUN /home/venv/bin/pip install gunicorn

# Copy project subdirectories to workdir
COPY app app
COPY tests tests

# Copy other top level files
COPY entrypoint.sh config.py decryptmessage.py run_tests.sh ./

# Make entry point and test files executable
RUN chmod ugo+x entrypoint.sh run_tests.sh

# Set some environment variables
ENV FLASK_APP=decryptmessage.py
ENV FLASK_ENV=production
ENV APP_SETTINGS=config.ProductionConfig

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]