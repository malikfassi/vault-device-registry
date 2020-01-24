#!/usr/bin/env bash

set -euxo pipefail

build_deps=$(cat <<EOF
EOF
)

apt-get update
[[ -n ${build_deps} ]] && apt-get install -y ${build_deps}

pip install --upgrade pip pipenv

# Debug tools until we have our ledger-stretch-slim image
apt-get install -yq curl netcat iputils-ping iproute2 lsof procps vim

# remove dev deps & builds tools
[[ -n ${build_deps} ]] && apt-get remove --purge ${build_deps} -y
apt-get clean
rm -rf -- /var/lib/apt/lists/*

exit 0
