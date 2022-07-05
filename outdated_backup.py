def main():
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
    #iniciate loop
    while True:
        date_input = input("Date: ").strip().split("/")
        if len(date_input) == 1:
            month, day, year = date_input[0].split(" ")
            try:
                if "," not in day:
                    continue
                day = day.replace(',','')
                #if data is valid
                if (month in months and day.isdigit() and year.isdigit()):
                    #check for valid days and year
                    if 1 <= int(day) <= 31 and len(year) == 4:
                        #print result
                        print(f"{year}-{int(months[month]):02}-{int(day):02}")
                        break
            except :
                pass
        else:
            try:
                if (date_input[0].isdigit() and date_input[1].isdigit() and date_input[2].isdigit()):
                    if 1 <= int(date_input[1]) <= 31 and len(date_input[2]) == 4 and 1 <= int(date_input[0]) <= 12:
                        print(f"{date_input[2]}-{int(date_input[0]):02}-{int(date_input[1]):02}")
                        break
            except :
                pass


if __name__ == "__main__":
    main()