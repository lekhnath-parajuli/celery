from dataclasses import dataclass, field
import celery
import datetime
from typing import Union, Type
from celery.schedules import solar
from celery.schedules import crontab, maybe_schedule
from celery.beat import ScheduleEntry


schedule_type = Union[datetime.datetime, datetime.timedelta, crontab, solar, int, float]


@dataclass
class Entry:
    app: celery.Celery = field(default_factory=lambda: None)
    name: str = field(default_factory=lambda: None)
    schedule: schedule_type = field(default_factory=lambda: None)
    relative: bool = field(default_factory=lambda: False)
    args: list[any] = field(default_factory=lambda: [])
    kwargs: dict[str, any] = field(default_factory=lambda: {})
    options: dict[str, any] = field(default_factory=lambda: {})
    last_run_at: datetime.datetime = field(default_factory=lambda: None)
    total_run_count: int = field(default_factory=lambda: 0)


class ScheduleEntry(ScheduleEntry, Entry):
    def __init__(self, **kwargs) -> None:
        self.set_constants(**{**Entry().__dict__, **kwargs})
        self.set_variables(**{**Entry().__dict__, **kwargs})

    def set_constants(
        self,
        app: celery.Celery,
        task: celery.Task,
        name: str,
        args: list[any],
        options: dict,
        kwargs: dict,
        last_run_at: datetime.datetime,
        total_run_count: int,
        **_
    ):
        self.app = app
        self.task = task
        self.name = name
        self.args = args or []
        self.kwargs = kwargs or {}
        self.options = options or {}
        self.last_run_at = last_run_at or self.default_last_run_time()
        self.total_run_count = total_run_count or 0

    def set_variables(self, schedule: schedule_type, relative: bool, **_):
        self.schedule = maybe_schedule(schedule, relative, app=self.app)

    def default_last_run_time(self):
        return self.schedule.now() if self.schedule else self.app.now()

    def default_now(self):
        return self.schedule.now() if self.schedule else self.app.now()
