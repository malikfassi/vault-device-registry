#!/usr/bin/env bash

set -euxo pipefail

isort -rc -c src
black -c src
