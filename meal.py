def main():
    day_time = convert(input("What time is it? "))
    if 7 <= day_time <= 8:
        print("breakfast time")
    elif 12 <= day_time <= 13:
        print("lunch time")
    elif 18 <= day_time <= 19:
        print("dinner time")
    else:
        print("not food time you hungry dummy")


def convert(time):
    x = time.split(":")
    hours = float(x[0])
    minutes = float(x[1])
    time_n = hours + minutes / 60
    return time_n




if __name__ == "__main__":
    main()