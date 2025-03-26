def substrings(str):
    result = []
    for i in range(len(str)):
        for j in range(i+1, len(str)+1, 1):
            result.append(str[i:j])
    print(result)
    return result


expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
