#!/bin/sh

EXPOSE_PORT=8000

# until wget db:5432  -O /dev/null; do
#   >&2 echo "mysql is unavailable - sleeping"
#   sleep 3
# done

python3 /web/manage.py runserver 0.0.0.0:${EXPOSE_PORT}
