class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        prod = 1
        if k<=1:
            return 0
        for r in range(len(nums)):
            prod *= nums[r]
            while prod >= k:
                prod //= nums[left]
                left+=1
            res += (r-left+1)

        return res