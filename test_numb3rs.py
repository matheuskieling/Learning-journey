from numb3rs import validate

def test_string():
    assert validate("cat") == False

def test_outofRange():
    assert validate("256.1.1.1") == False

def test_valid():
    assert validate("1.1.1.1") == True
    assert validate("199.1.199.1") == True
    assert validate("123.1.1.1") == True
    assert validate("1.1.171.1") == True
    assert validate("192.168.1.1") == True

def test_firstbyte():
    assert validate("192.276.279.280") == False