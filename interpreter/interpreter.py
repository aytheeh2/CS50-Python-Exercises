expression = input("Expression : ")
expression = expression.lstrip().rstrip()#removing left 7 right whitespaces
x, y , z = expression.split(" ")#splitting string with whitespace as a separator
x=float(x)
z=float(z)

if y == "+":
    result=x+z
elif y=="-":
    result=x-z
elif y=="*":
    result=x*z
elif y=="/":
    result=x/z

print(f"{result:.1f}")

