# print number from 1 to 100

number = 1

while number <= 100:
    print(number)
    number += 1


# print number from 100 to 1


while number >= -1:
    print(number)
    number -= 1


# print the multiplication table of a number n

n = int(input("Enter a number for getting multiplication table : "))

i = 1

while i <= 10:
    print(f"{n}*{i} = ", n * i)
    i += 1


# print the elements of the following list using a loop : [1,4,9,16,25,36,49,64,81,100]

listNum = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

li = 0

while li < len(listNum):
    print(listNum[li])
    li += 1

# Search for a number x in this tuple using loop:  [1,4,9,16,25,36,49,64,81,100]

llli = 0
searchNumber = int(input("Enter the number which you are currently searching : "))

listSearch = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

while llli < len(listNum):
    if searchNumber == listSearch[llli]:
        print(
            "We have found your desire number. Your searching number is :", searchNumber
        )
        break
    llli += 1
else:
    print("We dont have find your number.", searchNumber)
