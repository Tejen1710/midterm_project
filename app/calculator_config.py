
from dataclasses import dataclass
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

@dataclass(frozen=True)
class Config:
    LOG_DIR: Path = Path(os.getenv("CALCULATOR_LOG_DIR", "var/log"))
    HISTORY_DIR: Path = Path(os.getenv("CALCULATOR_HISTORY_DIR", "var/history"))
    MAX_HISTORY_SIZE: int = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "5000"))
    AUTO_SAVE: bool = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
    PRECISION: int = int(os.getenv("CALCULATOR_PRECISION", "6"))
    MAX_INPUT: float = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1e12"))
    ENCODING: str = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
    LOG_FILE: Path = Path(os.getenv("CALCULATOR_LOG_FILE", "var/log/calculator.log"))
    HISTORY_FILE: Path = Path(os.getenv("CALCULATOR_HISTORY_FILE", "var/history/history.csv"))

def ensure_dirs(cfg: "Config"):
    cfg.LOG_DIR.mkdir(parents=True, exist_ok=True)
    cfg.HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    cfg.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    cfg.HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
