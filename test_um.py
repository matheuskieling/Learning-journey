from um import count

def test_onlyvalid():
    assert count("um") == 1

def test_mix():
    assert count("um bum") == 1

def test_special():
    assert count("um? um... um,") == 3

def test_caseinsensitive():
    assert count("Um um uM UM") == 4
