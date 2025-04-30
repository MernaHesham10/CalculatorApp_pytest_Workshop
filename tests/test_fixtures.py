import pytest
from calculator import Calculator

# --------------------------
# 2. Fixtures (Dependency Injection)
# --------------------------
    
class TestCalculatorFixtures:
    """Shows fixture usage for test setup/teardown."""
    
    @pytest.fixture
    def calc(self):
        print("\nCreating calculator instance")  # Setup
        yield Calculator()
        print("\nCleaning up calculator")  # Teardown
    
    def test_multiplication(self, calc):
        assert calc.multiply(3, 4) == 12