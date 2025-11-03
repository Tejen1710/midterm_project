import pytest
from app.operations import get_operation
from app.exceptions import OperationError

def test_root_zero_n():
    with pytest.raises(OperationError):
        get_operation("root")(8, 0)

def test_even_root_negative():
    with pytest.raises(OperationError):
        get_operation("root")(-8, 2)

def test_modulus_by_zero():
    with pytest.raises(OperationError):
        get_operation("modulus")(5, 0)

def test_int_divide_by_zero():
    with pytest.raises(OperationError):
        get_operation("int_divide")(5, 0)

def test_percent_div_zero():
    with pytest.raises(OperationError):
        get_operation("percent")(5, 0)
