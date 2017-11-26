# blockchainbot

Project to simulate bitcoin buying and selling

# Getting started

* Setup database, see database.sql for schema
* Copy config_example.yml to config.yml
* Run simulator.py

# packages used

pip install pyyaml
pip install psycopg2

# Setup postgres on macOs

* brew update
* brew install postgres
* pg_ctl -D /usr/local/var/postgres start

# Installing all requirements:

* `pip3 install -r requirements.txt`

# Running things

* simulator: `python3 -m simulator.py`
* server: `python3 -m server.server`
* test accounts: `python3 -m test.account`
