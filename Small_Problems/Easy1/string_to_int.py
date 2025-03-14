def string_to_integer(num_str):
    int = 0
    tens_place = 1
    for char in num_str[::-1]:
        int += (ord(char) - 48) * tens_place
        tens_place *= 10
    return int

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True


def hexadecimal_to_integer(hex_str):
    int = 0
    hex_dec = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
    }
    for char in hex_str:
        int *= 16
        int += hex_dec[char.casefold()] 
    return int

print(hexadecimal_to_integer('4D9f') == 19871)  # True
