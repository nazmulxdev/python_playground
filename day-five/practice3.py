# WAP to find the sum of first n numbers .(using while)

number = int(input("Enter the number which you want to get the sum: "))

i = 1
sum = 0

while i <= number:
    sum += i
    i += 1
print(f"The total sum of the first {number} number is :", sum)

# WAP to find the factorial of first n numbers using for loop

numberFact = int(input("Enter the number which you want to get factorial :"))

fact = 1

for el in range(1, numberFact + 1, 1):
    fact *= el

print(f"The factorial of the {numberFact} number is :", fact)
