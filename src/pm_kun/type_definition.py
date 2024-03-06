from datetime import date
from typing import TypedDict
from enum import Enum
from uuid import UUID


class Priority(Enum):
    低 = 0
    標準 = 1
    緊急 = 2


class Status(Enum):
    未着手 = 0
    対応中 = 1
    完了 = 2


class ToDo(TypedDict):
    id: str
    task: str
    status: Status
    period: date
    priority: Priority
