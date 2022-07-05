def main():
    plate = input("Plate: ")
    if is_valid(plate):
       print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ##first 2 must be letters
    ##min of 2 and max 6 char
    if 2 <= len(s) <= 6:
        ##fist two items must be letters
        if s[0].isalpha() and s[1].isalpha():
            ##loop through string
            for i,c in enumerate(s):
                if s[i].isalpha():
                    if i+1 < len(s):
                        if s[i+1] == "0":
                            return False
                elif s[i].isdigit():
                    if i+1 < len(s):
                        if s[i+1].isalpha():
                            return False
                else:
                    return False
            return True
        else:
            return False
    else:
        return False





    ##no periods, spaces or punctuation marks

if __name__ == "__main__":
    main()