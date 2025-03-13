def odd_ndx_doubler(list):
    result = []
    for i in range(len(list)):
        current_value = list[i]
        if i % 2 == 1:
            current_value *= 2
        result.append(current_value)
    return result

my_nums = [1, 2, 3, 4, 5, 6]
print(odd_ndx_doubler(my_nums))
print(my_nums)
            
