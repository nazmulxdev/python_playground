def fact(n):
    if n == 0 or n == 1:  # base case
        return 1
    return n * fact(n - 1)  # Recursion case


print(fact(3))


def show(n):
    if n == 0:
        return 0
    print(n)
    show(n - 1)


show(10)
