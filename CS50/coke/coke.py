due = 50  # Set the initial amount due to 50

while due != 0 and due>0:
    amt = int(input("Insert Coin : "))
    # Check if the inserted coin is valid (5, 10, or 25)
    if amt == 5 or amt == 10 or amt == 25 and due>0:
        due =due- amt  # Reduce the amount due by the inserted coin
        if due>=0:
            print("Amount Due: " + str(due))
        else:break
    elif amt != due:
        print("Amount Due: "+str(due))
print("Change Owed: "+str(abs(due)))
