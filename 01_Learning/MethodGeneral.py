class Pretty:
    def __init__(self, prefix):
        self.prefix = prefix
    def print_me(self,a,b,c):
        print(self.prefix, a, sep="")
        print(self.prefix, b, sep="")
        print(self.prefix, c, sep="")

class Odd:
    def __init__(self):
        self.x = 10
        self.y = 20
        self.__z = 30

    def pr(self):
        print('__z= ', self.__z)

o = Odd()
print(o.x)
print(o.y)
print(o.pr())
