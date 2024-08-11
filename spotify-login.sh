#!/bin/bash

source .env
cd spotify_data_collect
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python spotify_login.py