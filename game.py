import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1:
                break
        except ValueError:
            pass
    computer_num = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess >= 1:
                answer = is_win(guess, computer_num)
                print(answer)
                if answer != "Just right!":
                    continue
                else:
                    break
        except ValueError:
            pass

def is_win(g, n):
    result = ""
    if g == n:
        result = "Just right!"
    if g < n:
        result = "Too small!"
    if g > n:
        result = "Too large!"
    return result

if __name__ == "__main__":
    main()