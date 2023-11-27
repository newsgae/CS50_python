'''
class Jar:
    def __init__(self, capacity: int=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Deposit error")
        self.size = self.size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Withdraw error")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("@capacity.setter error")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("@size.setter error")
        self._size = size


def main():
    # jar = Jar()
    # print(jar)
    # jar.deposit(2)
    # print(jar)
    # jar.deposit(3)
    # print(jar)
    # jar.withdraw(2)
    # print(jar)

    jar = Jar()
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar.capacity)
    print(jar.size)

if __name__ == "__main__":
    main()


In a file called jar.py, implement a class called Jar with these methods:

   1. __init__ should initialize a cookie jar with the given capacity, which represents
        the maximum number of cookies that can fit in the cookie jar.
        If capacity is not a non-negative int, though,
            __init__ should instead raise a ValueError.

    2.__str__ should return a str with 🍪, where
        n is the number of cookies in the cookie jar.
            For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"

    3.deposit should add n cookies to the cookie jar.
        If adding that many would exceed the cookie jar’s capacity, though,
            deposit should instead raise a ValueError.

    4.withdraw should remove n cookies from the cookie jar. Nom nom nom.
        If there aren’t that many cookies in the cookie jar, though,
            withdraw should instead raise a ValueError.

    5.capacity should return the cookie jar’s capacity.
    6. size should return the number of cookies actually in the cookie jar, initially 0.

first must done:
     None
'''

class Jar:
    def __init__(self, capacity: int=12):
        # run validations to received arguments
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return self.size * '🍪'

    def withdraw(self, n: int):
        # run validations to received arguments
        if self.size < n:
            raise ValueError
        self.size = self.size - n

    def deposit(self, n: int):
        # run validations to received arguments
        if n > self.capacity:
            raise ValueError
        self.size  = self.size + n


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("@capacity.setter error")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("@size.setter error")
        self._size = size


def main():
    jar = Jar()
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)
    print(jar.capacity)
    print(jar.size)


if __name__ == "__main__":
    main()


# check50 cs50/problems/2022/python/jar
# submit50 cs50/problems/2022/python/jar