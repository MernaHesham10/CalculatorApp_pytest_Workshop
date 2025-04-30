from calculator import Calculator
# --------------------------
# 1. Simple Syntax (Class Style)
# --------------------------

class TestSimpleSyntax:
    
    def test_addition(self):
        assert Calculator().add(2, 3) == 5
        
    def test_subtraction(self):
        assert Calculator().subtract(5, 3) == 2