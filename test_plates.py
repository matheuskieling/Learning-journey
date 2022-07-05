import plates
from plates import is_valid


def test_alphabeginning():
    assert is_valid("CS50") == True
    assert is_valid("50") == False

def test_numberbeginning():
    assert is_valid("CS050") == False

def test_numbermiddle():
    assert is_valid("CS150A") == False

def test_lenght():
    assert is_valid("A") == False
    assert is_valid("ASOIFJAIOWJGOHJ") == False

def test_alphanum():
    assert is_valid("!@#$") == False
    assert is_valid("CS!@$") == False