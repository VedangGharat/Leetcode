class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Sum = 0
        average = 0
        for i in range(k):
            Sum += nums[i]
        maxAvg = Sum/k

        for i in range(k, len(nums)):
            # maxAvg = max(average, maxAvg)

            Sum += nums[i] - nums[i-k]
            Average = Sum/k
            maxAvg = max(Average, maxAvg)
        return maxAvg