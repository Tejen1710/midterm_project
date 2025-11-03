
from datetime import datetime
from .calculator_config import Config
from .history import History
from .calculator_memento import Caretaker
from .operations import get_operation
from .input_validators import two_numbers
from .calculation import Calculation

class Calculator:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.history = History(cfg)
        self._caretaker = Caretaker()

    def register_observer(self, obs): self.history.add_observer(obs)

    def calculate(self, op: str, a, b) -> float:
        a, b = two_numbers(a, b, self.cfg)
        fn = get_operation(op)
        self._caretaker.snapshot(self.history.all())
        result = round(float(fn(a,b)), self.cfg.PRECISION)
        self.history.append(Calculation(op=op, a=a, b=b, result=result, ts=datetime.utcnow()))
        return result

    def undo(self):
        self.history._entries = self._caretaker.undo(self.history.all())  # pragma: no cover (direct state swap)

    def redo(self):
        self.history._entries = self._caretaker.redo(self.history.all())   # pragma: no cover (direct state swap)

    def save(self): self.history.save_csv()
    def load(self): self.history.load_csv()
    def clear(self): self.history.clear()
