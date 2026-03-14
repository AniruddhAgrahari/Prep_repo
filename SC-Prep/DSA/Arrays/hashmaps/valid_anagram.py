
# Time complexity: O(n) - two passes through strings
# Space complexity: O(n) - dict stores atmost n unique characters

def is_anagram(s:str, t:str) -> bool:
    d = {}

    for char in s:
        d[char] = d.get(char, 0) + 1
    for char in t:
        d[char] = d.get(char, 0) - 1
    for value in d.values():
        if value != 0:
            return False
    
    return True






assert is_anagram("anagram", "nagaram") == True
assert is_anagram("rat", "car") == False
assert is_anagram("a", "a") == True