def count_max_adjacent_consonants(str):
    str_without_spaces = str.replace(" ", "")
    max_consonant_count = 0
    adjacent_consonants = ""
    for char in str_without_spaces.lower():
        if char not in ['a', 'e', 'i', 'o', 'u']:
            adjacent_consonants += char
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_consonants) > 1:
                    max_consonant_count = len(adjacent_consonants)
        else:
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_consonants) > 1:
                    max_consonant_count = len(adjacent_consonants)
            adjacent_consonants = ""
    return max_consonant_count


def sort_by_consonant_count(str_list):
    str_list.sort(key=count_max_adjacent_consonants, reverse=True)
    return str_list

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# Expected: ['dddaa', 'ccaa', 'aa', 'baa']
# Actual:   ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# Expected: ['salt pan', 'can can', 'batman', 'toucan']
# Actual:   ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# Expected: ['bar', 'car', 'far', 'jar']
# Actual:   ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# Expected: ['month', 'day', 'week', 'year']
# Actual:   ['day', 'week', 'month', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# Expected: ['xxxx', 'xxxb', 'xxxa']
# Actual:   ['xxxa', 'xxxx', 'xxxb']
