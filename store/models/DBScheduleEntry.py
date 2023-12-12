from Config import config
import sqlalchemy
from sqlalchemy import Column, String, Boolean, Integer, Timestamp
from sqlalchemy.dialects.postgresql import JSONB, UUID


class DBScheduleEntry(object):
    __table_args__ = {"schema": config.app_name}

    id = Column(
        "id",
        UUID(as_uuid=False),
        server_default=sqlalchemy.text("uuid_generate_v4()"),
        primary_key=True,
        index=True,
    )

    name = Column(String(255))
    args = Column(JSONB)
    kwargs = Column(JSONB)
    options = Column(JSONB)
    schedule = Column(JSONB)

    last_run_at = Column(Timestamp, server_default="now()")
    total_run_count = Column(Integer, server_default=1)
    relative = Column(Boolean, server_default="f")
