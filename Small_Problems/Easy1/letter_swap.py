def swap_chars(word):
    if len(word) == 1:
        return word
    swapped_word = word[len(word) - 1] + word[1:len(word) - 1] + word[0]
    return swapped_word

def swap(str):
    words = str.split()
    for i in range(len(words)):
        words[i] = swap_chars(words[i])
    result = ' '.join(words)
    return result


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
