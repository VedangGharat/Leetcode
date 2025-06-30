class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in nums_set:
            if i - 1 not in nums_set:
                start = 0
                while i + start in nums_set:
                    start += 1
                longest = max(longest, start)
        return longest