import random
while True:
    try:
        level_n = int(input("Level: ") )
        if level_n<=0:
            continue
        else:break
    except:
        pass
random_no= random.randint(1,level_n)
while True:
    try:
        guess = int(input("Guess: "))
        if guess<0:
            continue
        elif guess<random_no:
            print("Too small!")
            continue
        elif guess>random_no:
            print("Too large!")
            continue
        elif guess == random_no:
            print("Just right!")
            break
    except:
        pass