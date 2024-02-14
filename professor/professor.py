import random
def main():
    level_input=get_level()
    i=0
    score=0
    while i<10:
        x,y=generate_integer(level_input) # type: ignore
        print(f"{x}"+" + "+f"{y}"+" =",end="")
        try:
            ans = int(input())
            i+=1
            if x+y==ans:
                score+=1
                continue
            else:
                print("EEE")
                j=0
                while j<2:
                    try:
                        print(f"{x}"+" + "+f"{y}"+" =",end="")
                        ans=int(input())
                        j+=1
                        if x+y==ans:
                            score+=1
                            break
                    except:continue
                print(f"{x}" + " + " +f"{y}" + " =" + f"{x+y}")
                continue
        except:
            pass
    print("Score:",score)

def get_level():
    while True:
        try:
            level_N= int(input("Level :"))
            if level_N not in [1,2,3]:
                continue
            else: return level_N
        except: pass

def generate_integer(level):
    if level==1:
        x=random.randint(0,9)
        y=random.randint(0,9)
        return x,y
    elif level==2:
        x=random.randint(10,99)
        y=random.randint(10,99)
        return x,y
    elif level==3:
        x=random.randint(100,999)
        y=random.randint(100,999)
        return x,y


if __name__ == "__main__":
    main()