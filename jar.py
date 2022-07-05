class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0:
            self._capacity = capacity
            self._size = 0
        else:
            raise ValueError

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n + self._size <= self._capacity:
            self._size = self._size + n
            return self._size
        else:
            raise ValueError

    def withdraw(self, n):
        if self._size - n >= 0:
            self._size -= n
            return self._size
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    while True:
        try:
            user = input("Deposit, Withdraw, Print: ")
            if user == "D":
                try:
                    d_cookies = input("How many? ")
                    jar.deposit(int(d_cookies))
                except ValueError:
                    raise ValueError
            elif user == "W":
                try:
                    w_cookies = input("How many? ")
                    jar.withdraw(int(w_cookies))
                except ValueError:
                    raise ValueError
            elif user == "P":
                print(jar)

        except EOFError:
            exit("\n")


if __name__ == "__main__":
    main()
