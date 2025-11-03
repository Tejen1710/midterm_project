
from typing import List, Protocol
from datetime import datetime
import pandas as pd
from .calculation import Calculation
from .calculator_config import Config, ensure_dirs
from .exceptions import PersistenceError

class Observer(Protocol):
    def on_new_calc(self, calc: Calculation) -> None: ...

class History:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self._entries: List[Calculation] = []
        self._observers: List[Observer] = []

    def add_observer(self, obs: Observer): self._observers.append(obs)
    def clear(self): self._entries.clear()
    def all(self) -> List[Calculation]: return list(self._entries)

    def append(self, calc: Calculation):
        self._entries.append(calc)
        if len(self._entries) > self.cfg.MAX_HISTORY_SIZE:
            self._entries.pop(0)
        for obs in self._observers:
            obs.on_new_calc(calc)

    def to_df(self) -> pd.DataFrame:
        return pd.DataFrame([{
            "operation": c.op, "a": c.a, "b": c.b,
            "result": c.result, "timestamp": c.ts.isoformat()
        } for c in self._entries])

    def save_csv(self, path=None):
        ensure_dirs(self.cfg)
        p = path or self.cfg.HISTORY_FILE
        try:
            self.to_df().to_csv(p, index=False, encoding=self.cfg.ENCODING)
        except Exception as e:
            raise PersistenceError(f"Failed to save history to {p}") from e

    def load_csv(self, path=None):
        p = path or self.cfg.HISTORY_FILE
        try:
            df = pd.read_csv(p, encoding=self.cfg.ENCODING)
        except FileNotFoundError:
            return  # no-op if file doesn't exist
        except Exception as e:
            raise PersistenceError(f"Failed to read history from {p}") from e

        self._entries.clear()
        for _, row in df.iterrows():
            ts = datetime.fromisoformat(str(row["timestamp"]))
            self._entries.append(Calculation(
                op=str(row["operation"]), a=float(row["a"]), b=float(row["b"]),
                result=float(row["result"]), ts=ts
            ))
