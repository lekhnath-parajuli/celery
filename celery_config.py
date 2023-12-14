import redbeat
from Config import config
from kombu import Exchange, Queue


broker_heartbeat = 10
redbeat_lock_timeout = 60
beat_max_loop_interval = 10
redbeat_redis_url = config.redis_beat_url
beat_scheduler = f"{redbeat.__name__}.{redbeat.RedBeatScheduler.__name__}"

task_queues = (
    Queue("hi", Exchange("hi"), routing_key="hi"),
    Queue("bye", Exchange("bye"), routing_key="bye"),
    Queue("hello", Exchange("hello"), routing_key="hello"),
    Queue("welcome", Exchange("welcome"), routing_key="welcome"),
)
