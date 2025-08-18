class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # prefix = [nums[0]]
        # for i in range(1, len(nums)):
        #     prefix.append(prefix[-1]+nums[i])
        # return prefix
        if len(nums) <= 1:
            return nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums