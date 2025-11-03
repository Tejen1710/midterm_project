
import pytest
from app.calculator import Calculator
from app.calculator_config import Config
from app.exceptions import ValidationError

def mk():
    return Calculator(Config())

def test_calculate_and_history():
    c = mk()
    r = c.calculate("add", "2", "3")
    assert r == 5.0
    assert len(c.history.all()) == 1

def test_validation():
    c = mk()
    with pytest.raises(ValidationError):
        c.calculate("add", "abc", "1")

def test_undo_redo():
    c = mk()
    c.calculate("add", 1, 1)
    c.calculate("add", 2, 2)
    assert len(c.history.all()) == 2
    c.undo()
    assert len(c.history.all()) == 1
    c.redo()
    assert len(c.history.all()) == 2
