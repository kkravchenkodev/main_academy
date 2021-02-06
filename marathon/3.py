"""
Given a string, check if its characters can be rearranged to form a palindrome.
Where a palindrome is a string that reads the same left-to-right and right-to-left.

Example
"trueistrue" -> false;
"abcab" -> true because "abcba" is a palindrome

[input] string s (min 1 letters)
[output] boolean
"""


def is_palindrome(message):
    if len(message) == 1:
        return True
    dct = {}
    for ch in message:
        dct.setdefault(ch, 0)
        dct[ch] = dct[ch] + 1
    return len([x for x in dct.values() if x % 2]) in (0, 1)


print(is_palindrome("trueistrue"))  # False
print(is_palindrome("abcab"))       # True
print(is_palindrome("hello"))       # False
print(is_palindrome("hollo"))       # True
print(is_palindrome("racarrrac"))   # True

"""
	Test	Expected	Got	
print(isPalindrome("abb"))
True
True
print(isPalindrome("23332"))
True
True
print(isPalindrome("trueitrue"))
True
True
print(isPalindrome("trueistrue"))
False
False
print(isPalindrome("123123"))
True
True
print(isPalindrome("12312"))
True
True
print(isPalindrome("qqqrrr"))
False
False
print(isPalindrome("qqqrrrwww"))
False
False
print(isPalindrome("A"))
True
True
"""