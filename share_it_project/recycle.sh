#!/usr/bin/env bash
echo Starting Recycle...
rm db.sqlite3
rm shareIt/migrations/00*
python manage.py makemigrations
python manage.py migrate
echo running population script...
python populate_shareIt.py
