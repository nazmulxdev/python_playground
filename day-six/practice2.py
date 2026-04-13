# Write a recursive function to calculate the sum of first n natural numbers


def calc_sum(n):
    if n == 0:
        return 0
    sum = n + calc_sum(n - 1)
    return sum


print(calc_sum(5))


# Write a recursive function to print all elements in a list


def elm_list(n, idx):
    if len(n) == idx:
        return 0
    print(n[idx])
    elm_list(n, idx + 1)


elm_list([1, 2, 3, 4, 5, 6, 7, 8], 0)
