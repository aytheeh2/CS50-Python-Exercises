from validator_collection import is_email
def main():
    print(validator(input("What's your email address?")))

def validator(s):
    if is_email(s):
        return r"Valid"
    else:
        return r"Invalid"
main()