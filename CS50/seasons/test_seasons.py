# check50 cs50/problems/2022/python/seasons

from seasons import minutes_lived

def test1():
    assert minutes_lived(2022,11,5)== "Four hundred fifty-two thousand, one hundred sixty minutes"
    assert minutes_lived(2001,10,16)== "Eleven million, five hundred twenty-five thousand, seven hundred sixty minutes"
def test2():
    assert minutes_lived(16,10,2001)=="Invalid Date"
def test3():
    pass
def main():
    test1()
    test2()
    test3()

if __name__=="__main__":
    main()


