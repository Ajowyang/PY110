def interleave(list1, list2):
    result = []
    #for i in range(len(list1)):
    #    result.append(list1[i])
    #    result.append(list2[i])
    #return result
    for item in zip(list1, list2):
        result.extend(list(item))
    print(result)
    return result

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
