# Test cases for testing main.py functions
import pytest
import sys
from main import Calci

sys.path.insert(0, "./")


@pytest.fixture
def calculation():
    return Calci(8, 2)


@pytest.fixture
def calculationSpecial():
    return Calci(8, 0)


class TestCalculations:
    def test_sum(self, calculation):
        assert calculation.sum() == 10
        assert calculation.sum() != 5

    def test_diff(self, calculation):
        assert calculation.difference() == 6
        assert calculation.difference() != 2

    def test_product(self, calculation):
        assert calculation.product() == 16
        assert calculation.product() != 10

    def test_quotient(self, calculation, calculationSpecial):
        assert calculation.division() == 4
        assert calculation.division() != 3
        assert calculationSpecial.division() == "Can't divide with zero"


# To run the test cases execute command python -m unittest
