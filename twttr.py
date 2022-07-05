def main():
    input_word = input("Input: ")
    print(f"Output: {shorten(input_word)}")

def shorten(word):
    output = word
    vowels = ["a", "e", "i", "o", "u"]
    for i in word:
        if i.lower() in vowels:
            output = output.replace(i, "")
    return output
if __name__ == "__main__":
    main()