class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        windowSize = 2*k+1
        if k == 0:
            return nums
        
        if n < windowSize:
            return [-1] * n
        
        presum = [nums[0]]
        for i in range(1, n):
            presum.append(presum[-1] + nums[i])

        averages = [-1] * k
    
        for i in range(k, len(nums)-k):
            inboundval = i+k
            outboundval = i-k-1
            if i-k == 0:
                averages.append(presum[inboundval] // windowSize)
            else:
                averages.append((presum[inboundval]-presum[outboundval]) // windowSize)
        
        for i in range(n-k, n):
            averages.append(-1)
        
        return averages
        

        
