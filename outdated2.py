def main():
    date_input = ["x"]
    while True:
        date_input = input("Date: ")
        if not date_input[1] == " ":
            if not date_input[7] == "/":
                date_input = final_list(date_input.strip())
                year = int(date_input[2])
                if date_input[0].isdigit():
                    month = int(date_input[0])
                elif date_input[0] in months:
                    month = int(months[date_input[0]])
                day = int(date_input[1])
                if (date_input[0] in months and date_input[1].isdigit() and date_input[2].isdigit()) or (date_input[0].isdigit() and date_input[1].isdigit() and date_input[2].isdigit()):
                    if 1 <= day <= 31 and 1 <= month <= 12:
                        break
            else:
                break
        exit()
    if day < 10:
        day = "0" + str(day)
    if month < 10:
        month = "0" + str(month)
    print(f"{year}-{month}-{day}", end="")

def remove_char(x, char):
    date_final = ""
    new_date = ""
    date_input = x
    date_input = date_input.split(char)
    new_date += " ".join(date_input)
    date_final = new_date
    return date_final

def final_list(x):
    y = remove_char(x, "-")
    y = remove_char(y, ",")
    y = remove_char(y, "/")
    y = y.split()
    return (y)


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

