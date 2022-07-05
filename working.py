import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"([0-9]|[1][0-2]):?([0-5][0-9])? (AM|PM)+( to )+([0-9]|[1][0-2]):?([0-5][0-9])? (AM|PM)+", s):
        first, last = matches[1], matches[5]
        if matches[3] == "PM":
            first = int(first) + 12
            if first == 24:
                first = "12"
        if matches[7] == "PM":
            last = int(last) + 12
            if last == 24:
                last = "12"
        if matches[7] == "AM" and last == "12":
            last = "00"
        if matches[3] == "AM" and first == "12":
            first = "00"
        if matches[2] and matches[6]:
            return f"{int(first):02}:{matches[2]}{matches[4]}{int(last):02}:{matches[6]}"
        elif matches[2] and not matches[6]:
            return f"{int(first):02}:{matches[2]}{matches[4]}{int(last):02}:00"
        elif not matches[2] and matches[6]:
            return f"{int(first):02}:00{matches[4]}{int(last):02}:{matches[6]}"
        elif not matches[2] and not matches[6]:
            return f"{int(first):02}:00{matches[4]}{int(last):02}:00"

    else:
        raise(ValueError)


if __name__ == "__main__":
    main()


