def leading_substrings(str):
    result = []
    for i in range(len(str)):
        result.append(str[0:i+1])
    return result

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
