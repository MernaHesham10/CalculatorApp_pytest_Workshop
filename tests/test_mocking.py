import pytest
from calculator import Calculator

# --------------------------
# 4. Mocking Tests (Isolated Testing)
# --------------------------

class TestMocking:    
    def test_api_call(self, mocker):
        # Mock an existing calculator method
        mock_add = mocker.patch(
            "calculator.Calculator.add",
            return_value=120
        )
        result = Calculator().add(100, 20)
        assert result == 120
        mock_add.assert_called_once_with(100, 20)