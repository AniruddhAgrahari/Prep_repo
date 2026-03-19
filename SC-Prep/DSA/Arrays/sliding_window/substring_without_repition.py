
# Time complexity - O(n)
# Space complexity - O(1) - bounded by fixed number of characters

def substring_without_repition(s):

    d = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in d:
            left = max(left, d[s[right]] + 1) 
            d[s[right]] = right
        else:
            d[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

    

print(substring_without_repition("abcb"))
print(substring_without_repition("pwwkew"))
print(substring_without_repition("bbbbb"))
print(substring_without_repition(""))
print(substring_without_repition("abba"))

