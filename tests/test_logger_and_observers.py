from pathlib import Path
from app.logger import get_logger
from app.calculator_config import Config
from app.history import History
from app.observers_impl import LoggingObserver, AutoSaveObserver
from app.calculation import Calculation
from datetime import datetime

def test_get_logger_and_logging(tmp_path):
    cfg = Config(LOG_DIR=tmp_path/'log', HISTORY_DIR=tmp_path/'hist',
                 LOG_FILE=tmp_path/'log'/'app.log',
                 HISTORY_FILE=tmp_path/'hist'/'h.csv')
    log = get_logger(cfg)
    hist = History(cfg)
    log_obs = LoggingObserver(cfg)
    hist.add_observer(log_obs)
    hist.append(Calculation(op="add", a=1, b=2, result=3, ts=datetime.utcnow()))
    assert Path(cfg.LOG_FILE).exists()
    assert Path(cfg.LOG_FILE).read_text(encoding=cfg.ENCODING)

def test_autosave_observer(tmp_path):
    cfg = Config(LOG_DIR=tmp_path/'log', HISTORY_DIR=tmp_path/'hist',
                 LOG_FILE=tmp_path/'log'/'app.log',
                 HISTORY_FILE=tmp_path/'hist'/'h.csv',
                 AUTO_SAVE=True)
    hist = History(cfg)
    auto = AutoSaveObserver(hist, cfg)
    hist.add_observer(auto)
    hist.append(Calculation(op="add", a=1, b=2, result=3, ts=datetime.utcnow()))
    assert Path(cfg.HISTORY_FILE).exists()
