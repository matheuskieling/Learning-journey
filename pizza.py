from tabulate import tabulate
import csv
from sys import argv

if len(argv) == 2:
    try:
        if argv[1].endswith(".csv"):
            with open(argv[1]) as csvfile:
                file = csv.reader(csvfile)
                print(tabulate(file, headers="firstrow", tablefmt="grid"))
        else:
            exit("Not a CSV file")
    except FileNotFoundError:
        exit("File dos not exist")

elif len(argv) < 2:
    exit("Too few command-line arguments")

else:
    exit("Too many command-line arguments")