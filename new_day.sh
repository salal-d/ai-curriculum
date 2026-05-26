#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./new_day.sh <day_number>"
  exit 1
fi

DAY="day$1"

mkdir "$DAY"
cd "$DAY"

python3 -m venv .venv --without-pip
source .venv/bin/activate
curl -sS https://bootstrap.pypa.io/get-pip.py | python3
pip install anthropic python-dotenv

cp ../day6/.env .env

echo "Day $1 ready. You're in $DAY with venv active and packages installed."

