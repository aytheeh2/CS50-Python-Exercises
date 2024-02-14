# from PIL import Image,ImageOps
# import sys
# import os
# if len(sys.argv) == 3:
#     overlay = sys.argv[1]
#     user_img = sys.argv[2]
#     try:
#         overlay_extention = os.path.splitext(overlay)
#         user_img_extention = os.path.splitext(user_img)
#         if overlay_extention == user_img_extention :
#             if user_img_extention in [".jpg",".jpeg",".png"]:
#                 shirt = Image.open(overlay)
#                 shirt_size = shirt.size
#                 user_img = Image.open(user_img)
#                 user_img = ImageOps.fit(user_img,shirt_size,)
#                 user_img.paste(shirt,mask=shirt,box=None)
#                 user_img.save(sys.argv[2])
#             else :
#                 sys.exit("Input and output have different extensions")
#         else :
#             sys.exit("Invalid output")
#     except :
#         ...

# elif len(sys.argv) <3:
#     sys.exit("Too few command-line arguments")
# elif len(sys.argv) >3:
#     sys.exit("Too many command-line arguments")

from PIL import Image, ImageOps
import sys, os

shirt_pik = sys.argv[1]
user_pik = sys.argv[2]
shirt_pik_extention = os.path.splitext(shirt_pik)
user_pik_extention = os.path.splitext(user_pik)
if len(sys.argv) == 3:
    print("1 yes", shirt_pik_extention, user_pik_extention)
    if os.path.exists(shirt_pik):
        pass
    else:
        sys.exit("Input does not exist")
    if shirt_pik_extention[1] in [".jpg", ".jpeg", ".png"]:
        print("2 yes")
        if user_pik_extention[1] in [".jpg", ".jpeg", ".png"]:
            print("3 yes")
            if user_pik_extention[1] == shirt_pik_extention[1]:
                print("4 yes")
                try:
                    print("5 yes")
                    shirt_overlay = Image.open("shirt.png")
                    shirt_size = shirt_overlay.size
                    shirt_pikk = Image.open(shirt_pik)
                    user_shirt=ImageOps.fit(shirt_pikk,shirt_size)
                    user_shirt.paste(shirt_overlay,box=None,mask=shirt_overlay)
                    user_shirt.save(user_pik)
                except:
                    pass
            else:
                sys.exit("Input and output have different extentions")
        else:
            sys.exit("Invalid output")
    else:
        sys.exit("Input does not exist")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
