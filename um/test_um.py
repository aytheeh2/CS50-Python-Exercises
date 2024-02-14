from um import count


def test_count1():
    assert count("um") == 1


def test_count2():
    assert count("um, um. yamumy") == 2


def test_count3():
    assert count("Um, thanks") == 1
    assert count("m, thanks") == 0



def main():
    test_count1()
    test_count2()
    test_count3()


if __name__ == "__main__":
    main()
