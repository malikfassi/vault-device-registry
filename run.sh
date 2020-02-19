#!/usr/bin/env bash

source $(pipenv --venv)/bin/activate

set -euxo pipefail

# python migration.py run

if [ "$(uname)" == "Darwin" ]; then
    ini_file=uwsgi.mac.ini
else
    ini_file=uwsgi.ini
fi

python create_tables.py
exec uwsgi -H $(pipenv --venv) --ini ${ini_file}
