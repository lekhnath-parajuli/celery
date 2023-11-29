#!/bin/bash

celery -A background flower --loglevel=info --port=9000 --broker=redis://localhost:6379
