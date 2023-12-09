#!/bin/bash

celery -A background worker --loglevel=info -Q hi &
celery -A background worker --loglevel=info -Q bye &
celery -A background worker --loglevel=info -Q hello &
celery -A background worker --loglevel=info -Q welcome &
# to loc the terminal so that docker can continuously look into logs asynchronously
tail -f ${tty}
