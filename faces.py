def main():
    user_input = input().split()
    print(" ".join(convert(user_input)))
def convert(x):
    new_string = []
    for word in x:
        if word == ":)":
            new_string.append("🙂")
        elif word == ":(":
            new_string.append("🙁")
        else:
            new_string.append(word)
    return new_string

if __name__ == "__main__":
    main()