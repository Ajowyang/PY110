def signed_integer_to_string(num):
    if num == 0:
        print("0")
        return "0"
        
    positive = True
    result = ""
    if num < 0:
        positive = False
        num *= -1

    digit_dict = {
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
    while num != 0:
        quotient = num % 10
        num = num // 10
        result = digit_dict[quotient] + result
    if positive == True:
        result = "+" + result
    else:
        result = "-" + result
    #return "+" + result if positive == True else "-" + result   
    print(result)
    return result

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
