items = {}
try :
    while True:
        item = input().upper()
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1
except EOFError:
    pass
print("")
for item ,count in sorted(items.items()):
    print(f"{count} {item}")