count = 1

while count <= 5:
    count += 1
    print("Nazmul")

print(count)

i = 1
while i <= 10:
    print(i)
    i += 1


# for loop

list = [1, 2, 3]

for el in list:
    print(el)
else:
    print("end")


tup = ("ali", 220, "express")

for val in tup:
    print(val)
else:
    print("End tup")


rangeValue = int(input("Enter the start value: "))

stop_where = int(input("Enter where it will be stop: "))

increment = int(input("Enter the increment or decrement how to grow or fall :"))

for el in range(rangeValue, stop_where, increment):
    print(el)
