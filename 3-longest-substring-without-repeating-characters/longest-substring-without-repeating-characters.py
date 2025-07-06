class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 0
        check = []
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l+=1
            check.append(s[r])
            max_length = max(max_length, r-l+1)
        return max_length