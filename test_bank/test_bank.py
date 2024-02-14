from bank import value

def test_value():
    assert value("hello") == 0
    assert value("hmam") ==20
    assert value("qwee") == 100
    assert value("Hello") == 0
    
