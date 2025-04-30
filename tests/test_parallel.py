import pytest
from calculator import Calculator

# --------------------------
# 8. Parallel Execution
# --------------------------

@pytest.mark.parallel
class TestParallelExecution:
    """Tests designed for parallel execution."""
    
    @pytest.mark.parametrize("value", range(10))
    def test_square_operations(self, value):
        assert Calculator().multiply(value, value) == value ** 2

# --------------------------
# to run the class => pytest -n 4 test_parallel.py
# --------------------------