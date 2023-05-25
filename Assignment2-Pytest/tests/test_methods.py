import pytest


@pytest.fixture
def value():
    return "some text"


@pytest.fixture
def otherValue():
    return "some other value"


class TestStringMethods:
    def test_upper(self, value):
        assert value.upper() == "SOME TEXT"
        assert value.upper() != "some text"

    def test_split(self, value):
        assert value.split() == ["some", "text"]
        with pytest.raises(TypeError):
            value.split(2)

    def test_equal(self, value):
        assert value == "some text"
        assert value != otherValue

    def test_in(self):
        myList = [2, 4, 6, 8, 10]
        assert 2 in myList
        assert 3 not in myList
