from datetime import date, timedelta
import inflect
import sys

p = inflect.engine()

def main():
        sing = get_string(input('Date of Birth: '))
        print(sing)


def get_string(s):
    try:
        b_date = date.fromisoformat(s)
        today = date.today()
        difference = today - b_date
        second_difference = timedelta.total_seconds(difference)
        minute_difference = second_difference/60
        final_string = str(p.number_to_words(int(minute_difference))) + " minutes"
        demon = " and"
        if demon in final_string:
            final_string = final_string.replace(demon, "")
        return final_string.capitalize()
    except ValueError:
        sys.exit(1)


if __name__ == "__main__":
    main()
