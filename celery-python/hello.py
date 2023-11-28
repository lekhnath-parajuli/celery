from celery import Celery
from time import sleep

app = Celery('sidekick', broker='redis://redis:6379/0', backend='rpc://', task_default_queue='hello')

@app.task
def hello(task_id):
    sleep(2)
    return f"hello {task_id} completed!"