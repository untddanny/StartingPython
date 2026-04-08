class Solution(object):
    def isPalindrome(self, x):
        original = str(x)
        reversed = original[::-1]
        return original == reversed
