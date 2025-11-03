import pytest
from app.input_validators import coerce_number
from app.calculator_config import Config
from app.exceptions import ValidationError

def test_coerce_too_large_value():
    cfg = Config(MAX_INPUT=10.0)
    with pytest.raises(ValidationError):
        coerce_number(11.0, cfg)
