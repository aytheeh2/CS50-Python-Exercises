greet = input("Greeting : ")
greet=greet.lower().lstrip().rstrip()
if greet[0] != "h":
    print("$100")
elif (greet[0] == "h") and (greet[1:5] != "ello"):
    print("$20")
elif (greet[0] == "h") and (greet[1:5] =="ello"):
    print("$0")
