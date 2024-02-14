from numb3rs import validate

def test_validate_True():
    assert validate("1.20.220.255") == True
    assert validate("255.255.255.255") == True
    assert validate("2.5.25.255") == True
def test_validate_False():
    assert validate("1.320.220.255") == False
    assert validate("256.255.255.255") == False
    assert validate("2.5.258.255") == False

def main():
    test_validate_False()
    test_validate_True()

if __name__ =="__main()":
    main()