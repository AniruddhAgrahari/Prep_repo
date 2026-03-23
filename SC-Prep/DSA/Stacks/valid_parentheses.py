

def isValid(s:str) -> bool:
    stack = []
    pairs = {")":"(", "]":"[", "}":"{"}

    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack:
                return False
            if pairs[char] == stack[-1]:
                stack.pop()
            else:
                return False
    return not stack


print(isValid("()"))      # Expected: True
print(isValid("()[]{}"))  # Expected: True
print(isValid("(]"))      # Expected: False
print(isValid("([)]"))    # Expected: False
print(isValid("{[]}"))    # Expected: True