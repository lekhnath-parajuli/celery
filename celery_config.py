from kombu import Exchange, Queue


worker_pool = "solo"
broker_heartbeat = 10
redbeat_lock_timeout = 12 * 30 * 24 * 60 * 60
beat_max_loop_interval = 10
broker_connection_retry = 120
broker_connection_retry_on_startup = None
broker_connection_max_retries = None

task_queues = (
    Queue("hi", Exchange("hi"), routing_key="hi"),
    Queue("bye", Exchange("bye"), routing_key="bye"),
    Queue("hello", Exchange("hello"), routing_key="hello"),
    Queue("welcome", Exchange("welcome"), routing_key="welcome"),
)
