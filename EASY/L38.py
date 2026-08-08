'''

'''


class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        r = ""
        for char in s:
            if char.isalnum():
                r+=char
        return r == r[::-1]
        