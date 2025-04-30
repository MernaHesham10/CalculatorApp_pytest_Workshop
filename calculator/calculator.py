class Calculator:
    """A simple calculator class."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
class CurrencyConverter:
    @staticmethod
    def get_rate(from_curr, to_curr):
        # Actual implementation
        return 1.0    