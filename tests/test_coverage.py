import pytest
from calculator import Calculator

# --------------------------
# 9. Test Coverage
# --------------------------

class TestEdgeCases:
    """Tests to improve code coverage."""
    
    def test_divide_negative(self):
        assert Calculator().divide(-10, 2) == -5
        
    def test_divide_float_result(self):
        assert Calculator().divide(5, 2) == 2.5

# --------------------------
# to run the class => pytest --cov=calculator test_coverage.py
# --------------------------