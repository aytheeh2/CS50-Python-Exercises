while True:
    try:
        x,y=str.split(input("Fraction: "),sep="/")
        if "."in x or "." in y:
            continue
        x = float(x)
        y = float(y)
        if x > y:
            continue
        # print("x and y are",x,y)
        # print(type(x),type(y))
        if ((x/y)*100.0) <=1.0:
            print("E")
            break
        elif ((x/y)*100.0) <99.0:
            print(str(round((x/y)*100.0))+"%")
            break
        elif ((x/y)*100.0) >= 99.0:
            print("F")
            break
        else:continue
    except(ZeroDivisionError):
        # print("div by 0")
        continue
    except(ValueError):
        # print("value err")
        continue