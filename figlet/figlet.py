import random
from pyfiglet import Figlet
import sys
figlet = Figlet()
if len(sys.argv)==1:
    txt = input("Input: ")
    # f=random.choice(figlet.getFonts())
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(txt))
elif len(sys.argv)==3:
    if str(sys.argv[1]) == "-f" or str(sys.argv[1]) == "--font":
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
            txt = input("Input: ")
            print(figlet.renderText(txt))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
