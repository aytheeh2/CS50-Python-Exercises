import inflect
p=inflect.engine()
txt = []
while True:
    try:
        name=(input("Name: "))
        txt.append(name)
    except EOFError:
        break
output=p.join(txt)
print("Adieu, adieu, to "+output)