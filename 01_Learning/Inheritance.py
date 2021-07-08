class Person:
    def __init__(self, name,age,height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"

    def get_oldere(years):
        self.age += years


class Worker(Person):
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height) # access the __init__ from Person class
        self.salary = salary # individual information of worker

    def __str__(self): #overwriting the Person function with Worker function
        text = super(Worker, self).__str__()
        text += f", Salary: {self.salary}"
        return text

    def calc_yearly_salary(self):
        return self.salary * 12


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"


worker1 = Worker("Henry", 40, 176, 3000)
print(worker1)
print(worker1.calc_yearly_salary())

v1 = Vector(2,5)
v2 = Vector(6,3)

print(v1)
print(v2)

v3 = v1 + v2
print(v3)