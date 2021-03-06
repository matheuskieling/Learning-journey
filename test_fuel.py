import pytest
import fuel
from fuel import convert, gauge

def test_convert():
    assert convert("1/4") == 25

def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_valueerror():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("101/1")

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"