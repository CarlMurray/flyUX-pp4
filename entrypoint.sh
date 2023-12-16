#!/bin/bash

python manage.py migrate
python manage.py loaddata fixtures/airports.json fixtures/aircraft.json fixtures/flights.json fixtures/blogposts.json
python manage.py collectstatic
python manage.py runserver 0.0.0.0:8500
