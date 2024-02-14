word = input("camelCase : ")
converted=""
for letter in word:
    if letter.islower():
        converted=converted+letter
    elif letter.islower()!=True:
        converted=converted+"_"
        converted=converted+letter.lower()

print("snake_case : "+converted)
