import celery.beat as parent_beat


class PersistentScheduler(parent_beat.PersistentScheduler):
    _store = {"tz": "UTC", "utc_enabled": True}

    # def _next_instance(self, last_run_at=None):
    #     print("this is it")
    #     return None
    # __next__ = next = _next_instance

    # def scheduler(self):
    #     return self

    def tick(self, *args, **kwargs):
        # print("checking")
        super().tick(self, *args, **kwargs)

    def setup_schedule(self):
        self._store.setdefault("entries", {})
        self.schedule["db-task"] = self.Entry(
            app=self.app, name="db-task", task="tasks.hi.hi", schedule=5, args=(2,)
        )

    # self.merge_inplace(self.app.conf.beat_schedule)

    # known_suffixes = ".db"
    # persistence = StoreManager

    # def setup_schedule(self):
    #     print("setup scheduler called")
