import celery.beat as parent_beat


class Scheduler(parent_beat.Scheduler):
    ...
