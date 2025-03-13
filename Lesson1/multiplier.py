def multiply(numlist, multiplier):
    result = []
    for i in range(len(numlist)):
        result.append(numlist[i] * multiplier)
    return result

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]
