class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print(self.name, self.age)

p1 = Person("kim", 100)
p1.myfun()
p1.age = 101
p1.myfun()

p1.name = "lee"
p1.myfun()

