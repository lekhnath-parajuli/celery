from celery import Celery
from time import sleep

app = Celery('sidekick', broker='redis://redis:6379/0', backend='rpc://', task_default_queue='hi')

@app.task
def hi(task_id):
    sleep(2)
    return f"hi {task_id} completed!"