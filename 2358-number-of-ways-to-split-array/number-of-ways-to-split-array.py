class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        total = sum(nums)
        
        for i in range(len(nums)-1):
            left += nums[i]
            right = total - left
            if left >= right:
                ans += 1
        return ans

