import re
def parse(s):
    check_iframe=re.search(r'<iframe\s(?:.*)</iframe>',s)
    if check_iframe:
        match = re.search(r'(?:<iframe\s)?.*(?:https?://)?.*(?:youtube.com/embed/)+([\w]+).*',s)
        if match:
            # print("YEs")
            # print(r"https://youtu.be/"+match.group(1))
            return r'https://youtu.be/'+match.group(1)
        else:
            # print("No")
            return None
    else:return None

def main():
    print(parse(input("HTML: ")))

if __name__ == "__main__":
    main()