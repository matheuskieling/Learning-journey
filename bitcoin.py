import requests
import json
from sys import argv
def main():
    prompt = len(argv)
    if prompt != 2:
        if prompt < 2:
            exit("Missing command-line argument")
        else:
            exit()
    else:
        try:
            amount = float(argv[1])
        except:
            exit("Command-line argument is not a number")

        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        except requests.RequestException:
            pass
        price_string = response["bpi"]["USD"]["rate"]
        formatted_number = format_rate(price_string)
        result = formatted_number * amount
        print(f"${result:,.4f}")


def format_rate(s):
    new_string = s.replace(",", "")
    decimal_list = new_string.split(".")
    decimal = float(decimal_list[1]) / (10 ** len(decimal_list[1]))
    number = float(decimal_list[0]) + decimal
    return number


if __name__ == "__main__":
    main()
