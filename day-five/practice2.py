# Print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]

numList = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in numList:
    print(num)
else:
    print("All value of the list has been printed.")

# Search for a number in this tuple using loop:[1,4,9,16,25,36,49,64,81,100]

tupValue = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

search_number = int(input("Enter the number which you are currently searching : "))

for num in tupValue:
    if search_number == num:
        print(
            "Congratulations , you have successfully founded your desire number :", num
        )
        break
else:
    print(
        "Sorry, your desire number is not listed our current list. We will be add this in later."
    )
