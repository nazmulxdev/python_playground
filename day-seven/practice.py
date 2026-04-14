# Create a new file "practice.txt" using python . Add the following data in it:

# Hi everyone
# We are learning File I/O
# using Java.
# I like programming in java


with open("day-seven/practice.txt", "a+") as f:
    f.write("Hi everyone")
    f.write("\nwe are learning file i/o")
    f.write("\nusing java")
    f.write("\nI like programming in Java")

# WAF that replace all occurrences of "java" with "python" in above file.

with open("day-seven/practice.txt", "r+") as f:
    data = f.read()
    if len(data):
        if "java" in data or "Java" in data:
            data = data.replace("java", "python")
            data = data.replace("Java", "Python")
            f.seek(0)
            f.write(data)
            f.truncate()
        else:
            print("Failed to replace")
    else:
        print("There is no text exit inside the file.")
# Search if the word "learning" exists in the file or not

with open("day-seven/practice.py", "r") as f:
    data = f.read()
    if len(data):
        if "learning" in data:
            print("Learning is exist inside this file.")
        else:
            print("learning is not exit inside this file.")
    else:
        print("The file is empty")
