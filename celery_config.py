from beat.StoreScheduler import StoreScheduler
from kombu import Exchange, Queue


beat_scheduler = f"{StoreScheduler.__module__}:{StoreScheduler.__name__}"
task_queues = (
    Queue("hi", Exchange("hi"), routing_key="hi"),
    Queue("bye", Exchange("bye"), routing_key="bye"),
    Queue("hello", Exchange("hello"), routing_key="hello"),
    Queue("welcome", Exchange("welcome"), routing_key="welcome"),
)
