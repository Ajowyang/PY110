def double_consonants(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''.join([char * 2 if char.lower() not in vowels and char.isalpha() else char for char in str])
    return result

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
