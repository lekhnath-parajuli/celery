from kombu import Exchange, Queue


CELERY_QUEUES = (
    Queue("hi", Exchange("hi"), routing_key="hi"),
    Queue("bye", Exchange("bye"), routing_key="bye"),
    Queue("hello", Exchange("hello"), routing_key="hello"),
    Queue("welcome", Exchange("welcome"), routing_key="welcome"),
)
