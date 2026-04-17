import math

# Define a circle class to create a circle with radius r using the constructor

# Define an Area() method of the class which calculates the area of the circle
#  Defile a Perimeter () method of the class which allows you to calculate the perimeter of the circle


class Circle:
    def __init__(self, r):
        self.radius = r

    def Area(self):
        return round(math.pi * math.sqrt(self.radius), 2)

    def Perimeter(self):
        return round(math.pi * 2 * self.radius, 2)


circle1 = Circle(10)

print(circle1.Area())
print(circle1.Perimeter())


#  Define a Employee class with attributes role, department and salary. This class


class Employee:
    def __init__(self, role, department, salary):
        self.department = department
        self.salary = salary
        self.role = role

    def showDetails(self):
        return {"role": self.role, "department": self.department, "salary": self.salary}


# Create an Engineer class that inherits property from Employee and
#
# ###

employe1 = Employee("Engineer", "Construction", 10000)

print(employe1.showDetails())


class Engineer(Employee):
    def __init__(self, name, age):
        super().__init__(role="Engineer", department="IT", salary="75000")
        self.name = name
        self.age = age

    def showDetails(self):
        data = super().showDetails()
        data["name"] = self.name
        data["age"] = self.age
        return data


eng1 = Engineer("Nazmul", 25)

print(eng1.showDetails())


# Create a class called Order which stores item and its price
# Use Dunder function __gt__() to convey that :

# order1> order2 if price of order1> price of order2


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order):
        return self.price > order.price


order1 = Order("Coke", 100)
order2 = Order("Cigarets", 60)

print(order2 > order1)
