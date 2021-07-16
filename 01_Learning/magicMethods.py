class Point:
    big_prime_1 = 1200556037
    big_prime_2 = 2444555677

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        s = str(self.x) + ", "
        s += str(self.y)
        return s

    def __repr__(self):
        s = "Point(" + str(self.x) + ", "
        s += str(self.y) + ")"
        return s

    def __hash__(self):
        n = self.x * big_prime_1
        return (n + self.y) % big_prime_2

    def __bool__(self):
        return x and y


pt = Point(3, 4)

class Dog:
    def __init__(self,d):
        self.d = d

    def __gt__(self, other):
        """ Greater than (>). This method provides a less-than comparison through Rules of Symmetry.
        If a>b than b<a."""
        if type(other) == Dog:
            return self.d > other.d
        else:
            return self.d > other

    def __lt__(self, other):
        if type(other) == Dog:
            return self.d < other.d
        else:
            return self.d < other

    def __repr__(self):
        return "Dog(" + str(self.d) +")"

d1, d5, d10 = Dog(1), Dog(5), Dog(10)
a_list = [50, d5, 100 , d1, -20, d10,3]
a_list.sort()
print(a_list)
