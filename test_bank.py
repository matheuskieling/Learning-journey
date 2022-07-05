import bank
from bank import value

def test_hello():
    assert value("hello") == 0

def test_case():
    assert value("HELLO") == 0

def test_hi():
    assert value("hi") == 20


def test_else():
    assert value(", this is cs50") == 100
    assert value("asdfmovie") == 100

def test_invalid():
    assert value(" HELLO") == 100