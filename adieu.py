import inflect

p = inflect.engine()

def main():
    adieu = "Adieu, adieu, to"
    names_list = []

    while True:
        try:
            names_list.append(input("Name: "))
        except EOFError:
            print()
            break
    names = p.join(names_list)
    print(f"{adieu} {names}")


main()