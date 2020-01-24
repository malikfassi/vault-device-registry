#!/usr/bin/env bash

set -euxo pipefail

apt-get update
# build-essential to build uWSGI
apt-get install -y build-essential

pip install --upgrade pip pipenv
# Create venv dir to force pipenv to install in this location
mkdir .venv
pipenv install --skip-lock

exit 0
