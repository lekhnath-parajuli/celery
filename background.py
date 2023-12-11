from Config import config
from celery import Celery

from tasks.hi import hi
from tasks.bye import bye
from tasks.hello import hello
from tasks.welcome import welcome

app = Celery("sidekick", broker=config.redis_url, backend="rpc://")
app.config_from_object("celery_config")

# tasks
hello = app.task(hello, queue="hello")
hi = app.task(hi, queue="hi")
bye = app.task(bye, queue="bye")
welcome = app.task(welcome, queue="welcome")


if __name__ == "__main__":
    [(hi.delay(2), hello.delay(2), bye.delay(2), welcome.delay(2)) for i in range(1000)]
