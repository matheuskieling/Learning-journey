def main():
    fruit = input("Item: ").lower().strip()
    if fruit in calories_15:
        print_calories(15)
    elif fruit in calories_20:
        print_calories(20)
    elif fruit in calories_50:
        print_calories(50)
    elif fruit in calories_60:
        print_calories(60)
    elif fruit in calories_70:
        print_calories(70)
    elif fruit in calories_80:
        print_calories(80)
    elif fruit in calories_90:
        print_calories(90)
    elif fruit in calories_100:
        print_calories(100)
    elif fruit in calories_110:
        print_calories(110)
    elif fruit in calories_130:
        print_calories(130)


calories_15 = ["lemon"]
calories_20 = ["lime"]
calories_50 = ["avocado", "cantaloupe", "honeydew melon", "pineapple", "strawberries", "tangerine"]
calories_60 = ["grapefruit", "nectarine", "peach"]
calories_70 = ["plums"]
calories_80 = ["orange", "watermelon"]
calories_90 = ["grapes", "kiwifruit"]
calories_100 = ["pear", "sweet cherries"]
calories_110 = ["banana"]
calories_130 = ["apple"]

def print_calories(c):
    print(f"Calories {c}")


if __name__ == "__main__":
    main()