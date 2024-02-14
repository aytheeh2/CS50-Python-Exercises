def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    print("calling dolar to float")
    d=float(d.strip("$"))
    # print(d)
    return d


def percent_to_float(p):
    print("calling percnt to float")
    p=float(p.strip("%"))
    # print(p)
    return p/100


main()
