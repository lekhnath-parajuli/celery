from celery import Celery
import background_tasks

app = Celery("sidekick", broker="redis://redis:6379/0", backend="rpc://")
app.config_from_object("celeryconfig")
worker_queues = ','.join([queue.name for queue in app.conf.task_queues])

# tasks
hello = app.task(background_tasks.hello, queue="hello")
hi = app.task(background_tasks.hi, queue="hi")
bye = app.task(background_tasks.bye, queue="bye")
welcome = app.task(background_tasks.welcome, queue="welcome")