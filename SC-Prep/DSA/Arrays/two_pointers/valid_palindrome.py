def isPalindrome(s:str) -> bool:

    # Clean the string, store it in new string and then compare new_string with it's reverse
    # time complexity: O(n)
    # space complexity: O(n)
    # Pattern - string cleaning 
    
    new_string = ""
    for char in s:

        if char.isalnum():
            new_string += char.lower()

    if new_string == new_string[::-1]:
            return True
    else:
         return False




if __name__ == "__main__":
    assert isPalindrome("racecar") == True
    assert isPalindrome("A man a plan a canal Panama") == True
    assert isPalindrome("race a car") == False
    assert isPalindrome("") == True
    assert isPalindrome("0P") == False
    print("All tests passed")