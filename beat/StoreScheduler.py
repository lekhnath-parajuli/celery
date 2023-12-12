from beat.Scheduler import Scheduler
from beat.PersistentScheduler import PersistentScheduler
from beat.ScheduleEntry import ScheduleEntry


class StoreScheduler(PersistentScheduler, Scheduler):
    Entry = ScheduleEntry
