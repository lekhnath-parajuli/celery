from celery import Celery
from time import sleep


#  ** remaining work (celery -A runner inspect active)
#  ** start-worker (celery -A runner worker --loglevel=info)


# cache = StrictRedis(host="localhost", port=6379, db=0)
app = Celery('tasks', broker='redis://localhost:6379/0', backend='rpc://')
# app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')
#  remaining works len(app.control.inspect().reserved().get('celery@Mac.local'))

#@app.task
def hello(task_id):
    sleep(2)
    print(f'hello world {task_id}')

# create task without decorator

hello = app.task(hello)
app.tasks.register(hello)
