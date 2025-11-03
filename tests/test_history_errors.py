import pytest
from app.history import History
from app.calculator_config import Config
from app.exceptions import PersistenceError
from app.calculation import Calculation
from datetime import datetime

def test_load_no_file_is_noop(tmp_path):
    cfg = Config(HISTORY_FILE=tmp_path/'missing.csv', LOG_FILE=tmp_path/'app.log',
                 LOG_DIR=tmp_path, HISTORY_DIR=tmp_path)
    h = History(cfg)
    h.load_csv()
    assert h.all() == []

def test_save_csv_raises_on_bad_path(tmp_path):
    cfg = Config(HISTORY_FILE=tmp_path/'hist.csv', LOG_FILE=tmp_path/'app.log',
                 LOG_DIR=tmp_path, HISTORY_DIR=tmp_path)
    h = History(cfg)
    h.append(Calculation(op="add", a=1, b=2, result=3, ts=datetime.utcnow()))
    with pytest.raises(PersistenceError):
        h.save_csv(path=tmp_path)
