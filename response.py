from validator_collection import validators, checkers, errors

def main():
    print(validator(input("What's your e-mail adress? ")))

def validator(s):
    is_email_adress = checkers.is_email(s)
    if is_email_adress:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()