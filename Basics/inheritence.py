class Person:
    def __init__(self, fname,lname):
        self.firstname = fname
        self.lastname = lname
    def print_name(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, " to the class of ", self.graduationYear)


x = Student("Mike", "Jhon", 2026)

x.print_name()
    