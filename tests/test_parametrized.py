import pytest
from calculator import Calculator

# --------------------------
# 3. Parameterized Tests
# --------------------------

class TestParametrizedOperations:
    """Separate test cases for each operation type"""
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 2),    # Addition
        (5, 3, 2),     # Subtraction
        (3, 4, 12)     # Multiplication
    ])
    def test_operations(self, a, b, expected):
        calc = Calculator()
        if expected == a + b:
            assert calc.add(a, b) == expected
        elif expected == a - b:
            assert calc.subtract(a, b) == expected
        else:
            assert calc.multiply(a, b) == expected