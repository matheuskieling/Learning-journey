owed = 50
while owed > 0:
    print(f"Amount Due: {owed}")
    while True:
        coin = int(input("Insert coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            owed -= coin
            break
        else:
            print(f"Amount Due: {owed}")

print(-owed)
