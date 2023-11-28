#!/bin/bash

celery -A hello worker --loglevel=info &
celery -A hi worker --loglevel=info &