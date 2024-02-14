import sys
try:
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1]) as file:
                no_of_lines = 0
                for line in file:
                    if line.lstrip().startswith("#"):
                        continue
                    elif line.lstrip() == "":
                        continue
                    else:
                        no_of_lines+=1
            print(no_of_lines)
        else:sys.exit("Not a Python file")
    elif len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")

