def substrings(str):
    result = []
    for i in range(len(str)):
        for j in range(i+1, len(str)+1, 1):
            result.append(str[i:j])
    #print(result)
    return result

def is_palindrome(str):
    if len(str) < 2:
        return False
    left = 0
    right = len(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True

#def palindromes(str):
#    substrs = [substr for substr in substrings(str) if len(substr) >= 2]
#    result = []
#    for i in range(len(substrs)):
#        curr_str = substrs[i]
#        if is_palindrome(curr_str):
#            result.append(curr_str)
#    print(result)
#    return result

def palindromes(str):
    result = [substr for substr in substrings(str) if is_palindrome(substr)]
    return result

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True
