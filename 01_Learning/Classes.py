class Car:
    accel = 3.0
    mpg = 25

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age


class Cat:
    pass

car1 = Car()
car2 = Car()
car3 = Car()

print("car1.accel = ", car1.accel)
print("car1.mpg = ", car1.mpg)
print("car2.accel = ", car2.accel)
print("car2.mog = ", car2.mpg)

my_car = Car()
yr_car = Car()
my_car.accel = 5.0

print("my_car.accel: ", my_car.accel)

top_dog = Dog("WonderBoy", "Collie", 11)
print(top_dog.name, top_dog.breed, top_dog.age)

class Marriage:
    def __init__(self):
        self.wife = Person("f")
        self.husband = Person("m")

a_marriage = Marriage()

class Person:
    def __init__(self, gender):
        self.gender =gender
