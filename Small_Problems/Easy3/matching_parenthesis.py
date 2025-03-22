def is_balanced(str):
    parens = 0
    sqbrackets = 0
    curlybraces = 0
    for char in str:
        match char:
            case "(":
                parens += 1
            case ")":
                parens -= 1
            case  "[":
                sqbrackets += 1         
            case "]":
                sqbrackets -= 1
            case "{":
                curlybraces += 1
            case "}":
                curlybraces -= 1
        if parens < 0 or sqbrackets < 0 or curlybraces < 0:
            return False
    return parens == 0 and sqbrackets == 0 and curlybraces == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
