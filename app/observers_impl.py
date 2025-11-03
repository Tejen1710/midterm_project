
from .history import Observer
from .calculation import Calculation
from .calculator_config import Config
from .logger import get_logger

class LoggingObserver(Observer):
    def __init__(self, cfg: Config):
        self.log = get_logger(cfg)
    def on_new_calc(self, calc: Calculation) -> None:
        self.log.info(f"{calc.op} {calc.a} {calc.b} = {calc.result}")

class AutoSaveObserver(Observer):
    def __init__(self, history, cfg: Config):
        self.history = history
        self.cfg = cfg
    def on_new_calc(self, calc: Calculation) -> None:
        if self.cfg.AUTO_SAVE:
            self.history.save_csv()
