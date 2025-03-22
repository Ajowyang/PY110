def sequence(count, starting_num):
    result = []
    for i in range(count):
        if not result:
            result.append(starting_num)
        else:
            result.append(result[len(result) - 1] + starting_num)
    return result


print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True
