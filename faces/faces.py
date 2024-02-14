def main():
    convert()

def convert():
    string=input("entr string with emoji")
    string=string.replace(":)","🙂")
    string=string.replace(":(","🙁")
    print(string)


main()