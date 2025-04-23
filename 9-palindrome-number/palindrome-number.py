class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = str(x)[::-1]     
        return str(x) == (reverse)