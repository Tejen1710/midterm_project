
import logging
from .calculator_config import Config, ensure_dirs

def get_logger(cfg: Config) -> logging.Logger:
    ensure_dirs(cfg)
    logger = logging.getLogger("calculator")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(cfg.LOG_FILE, encoding=cfg.ENCODING)
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger
