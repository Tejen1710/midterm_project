
from .exceptions import ValidationError
from .calculator_config import Config

def coerce_number(x, cfg: Config) -> float:
    try:
        v = float(x)
    except Exception as e:
        raise ValidationError(f"Not a number: {x}") from e
    if abs(v) > cfg.MAX_INPUT:
        raise ValidationError(f"Value {v} exceeds max allowed {cfg.MAX_INPUT}")
    return v

def two_numbers(a, b, cfg: Config):
    return coerce_number(a, cfg), coerce_number(b, cfg)
