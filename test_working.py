import pytest
from working import convert

def test_valid():
    assert convert("9 AM to 10 AM") == "09:00 to 10:00"

def test_invalid():
    with pytest.raises(ValueError) as exc_info:
        assert convert("9AMto10AM")