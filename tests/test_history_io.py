
from app.calculator import Calculator
from app.calculator_config import Config
from pathlib import Path

def test_save_load(tmp_path):
    cfg = Config(
        LOG_DIR=tmp_path/"log",
        HISTORY_DIR=tmp_path/"hist",
        HISTORY_FILE=tmp_path/"hist"/"h.csv",
        LOG_FILE=tmp_path/"log"/"app.log",
    )
    c = Calculator(cfg)
    c.calculate("add", 1, 2)
    c.save()
    assert Path(cfg.HISTORY_FILE).exists()
    c.clear()
    c.load()
    assert len(c.history.all()) == 1
