""" tests/test_operations.py """

import pytest
from app.operations import (
    add,
    subtract,
    multiply,
    divide
    )

# Addition tests
def test_addition():
    assert add(3, 5) == 8
    assert add(0, 0) == 0
    assert add(5, -3) == 2
    assert add(-2, 6) == 4
    assert add(-2, -2) == -4

# Subtraction tests
def test_subtraction():
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0
    assert subtract(5, -3) == 8
    assert subtract(-2, 6) == -8
    assert subtract(-2, -2) == 0
    
# Multiplication tests
def test_multiplication():
    assert multiply(3, 5) == 15
    assert multiply(0, 0) == 0
    assert multiply(5, -3) == -15
    assert multiply(-2, 6) == -12
    assert multiply(-2, -2) == 4

# Division tests
def test_division():
    assert divide(3, 5) == 0.6
    assert divide(5, -3) == pytest.approx(-1.66, abs=1e-2)
    assert divide(-2, 6) == pytest.approx(-0.33, abs=1e-2)
    assert divide(-2, -2) == 1

    with pytest.raises(
            ValueError,
            match = "Division by zero is not allowed."
            ):
        divide(1, 0)

# # Modulus tests
# def test_mod():
#     assert mod(3, 1) == 0
#     assert mod(5, -3) == -1
#     assert mod(-2, 6) == 4
#     assert mod(-2, -2) == 0

#     with pytest.raises(
#             ValueError,
#             match = "Modulus by zero is not allowed."
#             ):
#         mod(3, 0)
