import sqlalchemy
from .base import metadata
import datetime

time = sqlalchemy.Table(
    "time",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("studentId", sqlalchemy.String, sqlalchemy.ForeignKey("users.hashId")),
    sqlalchemy.Column("date", sqlalchemy.DateTime),
    sqlalchemy.Column("time", sqlalchemy.Integer),
)