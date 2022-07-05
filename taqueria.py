def main():
    total = 0
    while True:
        try:
            item = input("Item: ").strip().title()
            if item in items:
                total += items[item]
                print(f"Total: ${total:.2f}")
        except KeyError:
            pass
        except EOFError:
            print()
            break




items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }




if __name__ == "__main__":
    main()