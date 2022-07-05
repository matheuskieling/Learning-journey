def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    new_d = ""
    for i in d:
        if i != "$":
            new_d += i
    return float(new_d)


def percent_to_float(p):
    new_p = ""
    for i in p:
        if i != "%":
           new_p += i
    return float(new_p)/100

if __name__ == "__main__":
    main()