def repeater(str):
    result = ""
    for char in str:
        result += char
        result += char
    return result

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
