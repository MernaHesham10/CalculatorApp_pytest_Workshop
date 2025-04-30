import pytest

@pytest.fixture
def shared_calculator():
    from calculator import Calculator
    return Calculator()