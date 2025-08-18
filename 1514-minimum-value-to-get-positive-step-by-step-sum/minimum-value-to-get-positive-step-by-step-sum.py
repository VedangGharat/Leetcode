class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minval = 0
        val = 0
        for n in nums:
            val += n
            minval = min(val, minval)
        
        return 1-minval #if minval < 1 else -1