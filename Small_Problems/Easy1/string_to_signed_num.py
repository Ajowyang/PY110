def string_to_signed_integer(num_str):
    positive = True
    result = 0
    if num_str[0] not in [str(num) for num in range(10)]:
        if num_str[0] == '-':
            positive = False
        num_str = num_str[1:]
    digit_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
    }
    for char in num_str:
        result *= 10
        result += digit_dict[char]
    if positive == False:
        result *= -1
    print(result)
    return result


print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
