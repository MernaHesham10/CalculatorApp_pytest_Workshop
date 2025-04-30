import pytest
from calculator import Calculator
import sys 

# --------------------------
# 10. Test Skip
# --------------------------

class TestSkippedFeatures:
    
    @pytest.mark.skip(reason="Feature in development")
    def test_exponentiation(self):
        assert Calculator().power(2, 3) == 8  # Future feature
        
    @pytest.mark.skipif(
        sys.version_info < (3, 8),  # Now works
        reason="Requires Python 3.8+"
    )
    def test_walrus_operator_usage(self):
        assert (result := Calculator().add(2, 3)) == 5