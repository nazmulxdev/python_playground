# WAP to ask the user to enter names of their 3 favorite movies and stories then in a list .

movies = [
    input("Enter your first favorite movie or story name: "),
    input("Enter your second favorite movie or story name: "),
    input("Enter your third favorite movie or story name: "),
]

print(movies)


# WAP to check if a list contains a palindrome of elements.

container = [1, 2, 3, 2, 1]

containerCopy = container.copy()
containerCopy.reverse()


if container == containerCopy:
    print("This is a palindromic list")
else:
    print("This is not a palindromic list.")


# WAP to count the number of students with the grade "A " the following tuple

studentGrade = ("C", "D", "A", "A", "B", "B", "A")

print(studentGrade.count("A"))


# Store the above value in a list and sort them from "A" to "D"

studentList = list(studentGrade)
studentList.sort()
print(studentList)
