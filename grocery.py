from collections import OrderedDict
def main():
    order = []
    while True:
        try:
            order.append(input().strip().upper())
        except EOFError:
            pass
            break
    list = {}
    for item in order:
        if not item in list:
            list[item] = 1
        else:
            list[item] += 1
    for item in sorted(list):
        print(list[item], item)
main()