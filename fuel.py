#

def main():
    frac = input("Fraction: ")
    frac = convert(frac)
    print(f"{gauge(frac)}")


def convert(fraction):
    try:
        fraction_list = fraction.split("/")
        x = int(fraction_list[0])
        y = int(fraction_list[1])
        if 0 <= x <= 100 and 0 <= y <=100:
            result = (int((x / y) * 100))
            if x <= y:
                return result
        else:
            raise ValueError
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError



def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif 2 <= percentage < 99:
        return f"{percentage}%"
    else:
        return "E"


if __name__ == "__main__":
    main()