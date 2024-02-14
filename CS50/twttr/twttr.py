name = str.lstrip(str.rstrip(input("Input : ")))
output=""
for i in name:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        True
    else:
        output = output+i
print("Output : "+output)
