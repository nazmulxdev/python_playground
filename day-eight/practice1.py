# Create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method of print the average


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def avg_mark(self):
        marks = self.marks
        avg = 0
        total_subject = 0
        if not marks:
            return 0

        for key, value in marks.items():
            avg += value
            total_subject += 1

        return avg / total_subject


s1 = Student("Md Nazmul Hossen", {"chemistry": 80, "Physics": 95, "Math": 92})


# Create Account class with 2 attributes-balance and account no. Create methods for debit,credit and print balance.


class Acount:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, money):
        if money <= self.balance:
            self.balance = self.balance - money
            return self.balance
        else:
            return "Not able to withdrow money"

    def credit(self, money):
        if money > 0:
            self.balance = self.balance + money
            return self.balance

    def get_balance(self):
        return self.balance


acc1 = Acount(1000, "Naz-123")

print(acc1.get_balance())

print(acc1.debit(500))
print(acc1.credit(5000))
