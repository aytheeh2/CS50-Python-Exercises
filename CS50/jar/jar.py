class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity less thn 0")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size*"🍪"

    def deposit(self, n):
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError("cant deposit over Capacity")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Cnt withdrw over capacity")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    j1 = Jar(10)
    j1.deposit(5)
    print(j1)
    j1.withdraw(2)
    print(j1.capacity)
    print(j1.size)
    # print(j1.capacity,j1.size)


if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/jar
