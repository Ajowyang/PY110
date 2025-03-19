def digit_list(int):
    curr_int = int
    result = []
    while curr_int > 0:
        result = [curr_int % 10] + result
        curr_int = curr_int // 10
    print(result)
    return result


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
    
