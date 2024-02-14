ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything ")
if str(42) == ans.lstrip().rstrip():
    print("Yes")
elif "forty two" == ans.lower():
    print("Yes")
elif "forty two" ==ans.lower().lstrip().rstrip().replace("-"," "):
    print("Yes")
else:print("No")