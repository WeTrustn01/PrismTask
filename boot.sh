#!/bin/sh
source venv/bin/activate
python3 -m flask db init
python3 -m flask db init
python3 -m flask db migrate -m "trades table"
python3 -m flask db upgrade
python3 -m flask run
