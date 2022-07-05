import csv
from sys import argv

if len(argv) == 3:
    try:
        with open(argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            with open(argv[2], "w") as after:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(after, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    if row != "":
                        full_name = row["name"].split(",")
                        first_name = full_name[1]
                        last_name = full_name[0]
                        house = row["house"]
                        writer.writerow({"first" : first_name.lstrip() , "last" : last_name, "house" : house})
    except FileNotFoundError:
        exit(f"Could not read {argv[1]}")
elif len(argv) < 3:
    exit("Too few command-line arguments")

else:
    exit("Too many command-line arguments")