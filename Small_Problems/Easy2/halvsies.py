def odd_halvsies(lst):
    result = [ lst[0:len(lst)//2 + 1], lst[len(lst)//2+1:len(lst)] ]
    print(result)
    return result

def even_halvsies(lst):
    result =  [ lst[0:len(lst)//2], lst[len(lst)//2:len(lst)] ]
    print(result)
    return result

def halvsies(lst):
    if len(lst) % 2 == 1:
        return odd_halvsies(lst)
    else:
        return even_halvsies(lst)

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
