import twttr
from twttr import shorten

def test_lowcase():
    assert shorten("twitter") == "twttr"
    assert shorten("meu deus do ceu") == "m ds d c"

def test_uppercase():
    assert shorten("TEM UM RATO AQUI") == "TM M RT Q"
    assert shorten("COISA FEIA") == "CS F"

def test_numbers():
    assert shorten("meu numero e 9932") == "m nmr  9932"

def test_ponctuation():
    assert shorten("TEM! UM R@TO AQUI") == "TM! M R@T Q"