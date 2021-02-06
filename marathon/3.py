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


if __name__ == '__main__':
    assert is_palindrome("abb") == True
    assert is_palindrome("23332") == True
    assert is_palindrome("trueitrue") == True
    assert is_palindrome("trueistrue") == False
    assert is_palindrome("123123") == True
    assert is_palindrome("12312") == True
    assert is_palindrome("qqqrrr") == False
    assert is_palindrome("qqqrrrwww") == False
    assert is_palindrome("A") == True
