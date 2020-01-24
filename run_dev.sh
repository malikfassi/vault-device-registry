#!/usr/bin/env bash

export $(cat .env.dev | xargs)
./run.sh
