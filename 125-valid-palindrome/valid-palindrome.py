class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(i.lower() for i in s if i.isalnum())
        return string == string[::-1]