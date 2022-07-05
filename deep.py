answer = input("What is the Answer to the Great Question of Life, the Universe, and EveryThing? ")
if answer.lower() == "forty two" or answer.lower() == "forty-two" or answer.strip() == "42":
    print("Yes")
else:
    print("No")