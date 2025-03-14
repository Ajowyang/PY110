def integer_to_string(num):
    result = ""
    digits_dict = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
    }
    while num > 0:
        result = digits_dict[num % 10] + result
        num = num // 10
    #print(result)
    if not result:
        return "0"
    return result

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(9) == "9") 
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True   
