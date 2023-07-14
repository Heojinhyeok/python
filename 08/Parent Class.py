class Person:

    fname = 'jinhyeok'
    lname = 'heo'

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.lname, self.fname)

x = Person('heo', 'jinhyeok')
x.printname()
