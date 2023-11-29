#!/bin/bash

celery -A background flower --loglevel=info --port=5555 --broker=redis://redis:6379
