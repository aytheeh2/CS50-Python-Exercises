file_name = input("File Name : ")
file_name = file_name.lower().rstrip().lstrip() #stripping away left and right whitespaces and then converting to lower case
file_name = file_name+" "#adding a whitespace to access last charector inputted [x:-1]
if file_name[-4:-1] == "gif":
    print("image/gif")
elif file_name[-4:-1] == "jpg":
    print("image/jpeg")
elif file_name[-5:-1] == "jpeg":
    print("image/jpeg")
elif file_name[-4:-1] == "png":
    print("image/png")
elif file_name[-4:-1] == "pdf":
    print("application/pdf")
elif file_name[-4:-1] == "txt":
    print("text/plain")
elif file_name[-4:-1] == "zip":
    print("application/zip")
else: print("application/octet-stream")
