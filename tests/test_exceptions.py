import pytest
from calculator import Calculator

# --------------------------
# 4. Exception Tests (Error Handling)
# --------------------------

class TestExceptionCases:
    """Validates error conditions."""
    
    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            Calculator().divide(10, 0)