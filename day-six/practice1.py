# WAP to print the length of a list  (list is the parameter)


def list_length(a):
    if isinstance(a, (list, tuple)):
        print(len(a))
    else:
        print("Please enter valid value.")


list_length(
    [
        1,
        2,
    ]
)

list_length(2)
list_length((2, 3, 4))

# WAP to print the elements of a list in a single line (list is the parameter)


def list_line(a):
    if isinstance(a, (tuple, list)):

        for el in a:
            print(el, end="")

    else:
        print("Please enter valid value")


list_line([2, 3, 3, 5, 5, "nazmul"])


def py_short(a):
    print(*a)


py_short([2, 3, 3, 5, 5, "nazmul"])

# WAP to find the factorial of n . (n is the parameter)


def find_fact(n):
    if isinstance(n, (int)) and n >= 0:
        fact = 1
        for el in range(1, n + 1):
            fact *= el
        else:
            print("Factorial is :", fact)
    else:
        print("Please enter non negative integer value")


find_fact(3)


# WAF to convert USD to BDT
def usd_bdt(usd):
    if isinstance(usd, (int, float)):
        print(f"${usd} in bdt is {usd*125} taka")
    else:
        print("PLease enter valid monet to convert into usd to bdt.")


usd_bdt(1)


# Check is even or odd


def check_even_odd(n):
    if isinstance(n, (int, float)):
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Enter a valid number to check the number is weather even or odd")


check_even_odd(2)
