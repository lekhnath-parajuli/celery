#!/bin/bash

celery -A background worker --loglevel=info -Q hi &
celery -A background worker --loglevel=info -Q bye &
celery -A background worker --loglevel=info -Q hello &
celery -A background worker --loglevel=info -Q welcome &
# lister for all the logs from all celery workers
tail -f ${tty}