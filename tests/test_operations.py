
import pytest
from app.operations import get_operation
from app.exceptions import OperationError

@pytest.mark.parametrize("op,a,b,exp", [
    ("add", 2,3,5), ("subtract", 3,2,1), ("multiply", 4,2,8),
    ("divide", 9,3,3), ("power", 2,3,8), ("modulus", 7,3,1),
    ("int_divide", 7,3,2), ("percent", 50, 200, 25.0), ("abs_diff", 5, 9, 4),
])
def test_ops(op, a, b, exp):
    assert get_operation(op)(a,b) == exp

def test_divide_by_zero():
    with pytest.raises(OperationError):
        get_operation("divide")(1,0)

def test_unknown_op():
    with pytest.raises(OperationError):
        get_operation("nope")
