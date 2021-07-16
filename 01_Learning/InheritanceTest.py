class people():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def me(self):
        print("My name is {}, I am a {} and {} years old.".format(self.name, self.gender, self.age))

    def call_out(self):
        self.me()

class worker(people):
    def __init__(self,name,gender, age, work):
        super().__init__(name, gender, age)
        self.work = work

    def me(self):
        super().me()
        print("Befor I forget... I'm a {}.".format(self.work))


p1 = people("Martin", "Man", 36)
w1 = worker("John", "man", 45, "Banker")
w2 = worker("Cath", "female", 23, "Assistant")

p1.call_out()
w1.call_out()
w2.call_out()