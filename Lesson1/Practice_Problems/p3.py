def set_unique_vals(set_one, set_two):
    result = {}
    result = set_one | set_two
    return result

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(set_unique_vals(a, b))
