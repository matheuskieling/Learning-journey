def main():
    while True:
        date_input = input("Date: ")
        split_date = date_input.strip().split("/")
        if len(split_date) == 1:
            month, day, year = split_date[0].split()
            try:
                if not "," in day:
                    continue
               z day = day.replace(",", "")
                if (month in months and day.isdigit() and year.isdigit()):
                    month = months[month]
                    if 1 <= int(day) <= 30 and len(year) == 4:
                        print(f"{int(year)}-{int(month):02}-{int(day):02}")
                        break
            except:
                pass
        else:
            try:
                month, day, year = date_input.split("/")
                if (month.isdigit() and day.isdigit() and year.isdigit()):
                    if 1 <= int(day) <= 30 and 1 <= int(month) <= 12:
                        print(f"{int(year)}-{int(month):02}-{int(day):02}")
                        break
            except:
                pass


months = {
    "January" : "1",
    "February" : "2",
    "March" : "3",
    "April" : "4",
    "May" : "5",
    "June" : "6",
    "July" : "7",
    "August" : "8",
    "September" : "9",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}

if __name__ == "__main__":

    main()

