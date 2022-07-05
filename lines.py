from sys import argv

def main():
    if len(argv) == 2:
        try:
            if argv[1].endswith(".py"):
                file = open(argv[1], "r")
            else:
                exit("Not a Python file")
        except FileNotFoundError:
            exit("File does not exist")
        count = 0
        for line in file:
            line = line.lstrip(" ")
            if not line.startswith("#"):
                if not line.startswith("\n"):
                    count += 1
        print(count)
    elif len(argv) < 2:
        exit("Too few command-line arguments")
    else:
        exit("Too many command-line arguments")

if __name__ == "__main__":
    main()