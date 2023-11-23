from yaaredis import StrictRedis
from celery import Celery


cache = StrictRedis(host="localhost", port=6379, db=0)
