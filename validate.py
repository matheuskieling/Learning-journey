import re

email = input("Whats your email? ").strip()

if re.search("^[\w\.]+@[\w][^_]+\.(edu|com)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")