# blockchainbot

Project to simulate bitcoin buying and selling

# Getting started

* Setup database, see database.sql for schema
* Copy config_example.yml to config.yml
* Run simulator.py

# Virtualenv

* `python3 -m venv venv`
* `source venv/bin/activate`

to deactivate, run

* `deactivate`

# packages used

* pip install pyyaml
* pip install psycopg2

Install everything in one go with:

`pip3 install -r requirements.txt`

# Setup postgres on macOs

* brew update
* brew install postgres
* pg_ctl -D /usr/local/var/postgres start

# Running things

* simulator: `python3 -m simulator.py`
* flask server: `python3 -m server`
* unit tests: `python3 -m unittest`
