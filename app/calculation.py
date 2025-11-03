
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Calculation:
    op: str
    a: float
    b: float
    result: float
    ts: datetime
