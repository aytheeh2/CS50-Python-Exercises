from plates import is_valid

def test_starting_with_letter():
    assert is_valid("AB12") == True
    assert is_valid("ab12") == True
    assert is_valid("1ab12") == False
    assert is_valid("11abas") == False
    assert is_valid("12") == False
    assert is_valid("ab") == True

def test_length():
    assert is_valid("as") == True
    assert is_valid("abcdefg") == False
    assert is_valid("a") == False

def test_numbr_in_middle():
    assert is_valid("a121a3") == False
    assert is_valid("aaa222") == True
    assert is_valid("aaa22a") == False

def test_zero():
    assert is_valid("cs04") == False
    assert is_valid("cs400") == True
    assert is_valid("cs0ab") == False
    assert is_valid("00ab12") == False

def test_punctuation():
    assert is_valid("a.sda.") == False
    assert is_valid("aaa.22") == False
    assert is_valid(".sd a") == False


