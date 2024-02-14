import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ...
    no_of_um = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(no_of_um)


if __name__ == "__main__":
    main()
