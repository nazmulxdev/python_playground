# WAP to check if a number entered by the user is odd or even

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("This number is even")

elif number % 2 != 0:
    print("This number is an odd number.")
else:
    print("The number is zero")

# WAP to find the greatest of 3 numbers entered by the user

print("Enter three number one by one and check the greater number.")
a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number: "))

if a > b:
    if a > c:
        print("The greatest number is :", a)
    else:
        print("The greatest number is :", c)
elif b > c:
    if b > a:
        print("The greatest number is :", b)
    else:
        print("The greatest number is :", a)
elif c > a:
    if c > b:
        print("The greatest number is :", c)
    else:
        print("The greatest number is :", b)
else:
    print("The number are equal")
# Wap to check if a number is a multiple of 7 or not
