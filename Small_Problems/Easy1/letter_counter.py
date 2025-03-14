def clean_word(str):
    result = ""
    for char in str:
        if char.isalpha():
            result += char
    return result

def word_sizes(str):
    result = {}
    words = str.split()
    for word in words:
        cleaned_word = clean_word(word)
        if len(cleaned_word) not in result:
            result[len(cleaned_word)] = 1
        else:
            result[len(cleaned_word)] += 1
    return result

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
