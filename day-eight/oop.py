class Student:
    name = "nazmul"


s1 = Student()


class Car1:
    color = "Black"
    model = "A15"
    brand = "Audi"


class New_Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calc_grade(self):

        if self.marks <= 30:
            print(f"{self.name}, you failed")
        else:
            print(f"{self.name}, You passed")


std1 = New_Student("nazmul", 50)
std1.calc_grade()


class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.acc = True
        print("Car Started")


c1 = Car()

c1.start()
