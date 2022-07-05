import random


def main():
    questions = 0
    score = 0
    user_level = get_level()
    while questions <= 9:
        x = generate_integer(user_level)
        y = generate_integer(user_level)
        result = x + y
        count = 0
        while count < 3:
            try:
                user_try = int(input(f"{x} + {y} = "))
                if user_try != result:
                    print("EEE")
                    count += 1
                    continue
                elif user_try == result:
                    score += 1
                    break

            except ValueError:
                pass
        print(f"{x} + {y} = {result}")
        questions += 1
    print(score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level < 1 or level > 3:
            continue
        else:
            return level

def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
    elif level == 2:
        number = random.randint(10, 99)
    else:
        number = random.randint(100, 999)

    return number

if __name__ == "__main__":
    main()