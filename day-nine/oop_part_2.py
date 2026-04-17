class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("namzul")


class Account:
    def __init__(self, acc_no, acc_pass):
        self.__acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self, pas):
        self.__acc_pass = pas


class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Stop car")


class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.brand = name


toy1 = ToyotaCar("prius", "electric")


class Fortune(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = Fortune("Dis")


class A:
    varA = "Welcome to class A"


class B:
    varB = "Welcome to class B"


class C(A, B):
    varC = "Welcome to class C"


c1 = C()


class Person:
    name = "Anonymous"

    # def changeName(self, name):
    #     self.__class__.name = name
    # self.__class__.name=name
    # Person.name=name
    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()

p1.changeName("Shim")

print(p1.name)
print(Person.name)


class marks:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.math + self.phy + self.chem) / 3) + "%"


marks1 = marks(100, 50, 60)

print(marks1.percentage)


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(f"The complex number is  {self.real}i+{self.img}j")

    def __add__(num1, num2):
        newReal = num1.real + num2.real
        newImg = num1.img + num2.img
        return Complex(newReal, newImg)


comp1 = Complex(5, 32)

comp2 = Complex(3, 9)

comp1.showNumber()

comp2.showNumber()


comp4 = comp2 + comp1

comp4.showNumber()
