from seasons import get_string
import pytest

def test_valid():
    assert get_string("2021-06-07") == "Five hundred twenty-five thousand, six hundred minutes"

def test_invalid():
    with pytest.raises(SystemExit) as exc_info:
        assert get_string("June 7th, 2021")