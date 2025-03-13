def letter_freq(str):
    result = {}
    for i in range(len(str)):
        if str[i] != " ":
            if str[i] in result.keys():
                result[str[i]] += 1
            else:
                result[str[i]] = 1
    return result

statement = "The Flintstones Rock"
print(letter_freq(statement))
