def validate(N):
    from re import search
    valid = search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",N)
    if valid:
        for i in range(1,5):
            if int(valid.group(i)) <= 255 and int(valid.group(i)) >=0:
                continue
            else : return False
        return True
    else : return False



def main():
    print(validate(input("IP: ")))

if __name__ == "__main()__":
    main()
