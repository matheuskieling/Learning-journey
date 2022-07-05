
string = input("camelCase: ")
new_string = []
for i in string:
    if i.islower():
        new_string.append(i)
    if i.isupper():
        new_string.append("_")
        i = i.lower()
        new_string.append(i)
print("".join(new_string))