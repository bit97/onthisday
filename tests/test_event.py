import pytest
from onthisday.event import Event


@pytest.mark.parametrize("test_input,expected", [((1900, False), 1900), ((0, False), 0), ((0, True), 0)])
def test_get_positive_year(test_input, expected):
    (year, bc) = test_input
    e = Event(year, "Dummy title", bc)

    assert e.get_year() == expected


@pytest.mark.parametrize("test_input,expected", [((44, True), -44), ((123, True), -123)])
def test_get_negative_year(test_input, expected):
    (year, bc) = test_input
    e = Event(year, "Dummy title", bc)

    assert e.get_year() == expected


def test_str_positive_year():
    e = Event(2006, "Italy wins world cup")

    assert str(e) == "[2006] Italy wins world cup"


def test_str_negative_year():
    e = Event(44, "The assassination of Julius Caesar takes place", True)

    assert str(e) == "[44 a.C.] The assassination of Julius Caesar takes place"


