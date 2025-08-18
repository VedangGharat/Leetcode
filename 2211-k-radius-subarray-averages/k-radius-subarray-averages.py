class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        if 2*k+1 > len(nums):
            return [-1] * (len(nums))
        

        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1] + nums[i]) 
            # prefix.append(prefix[i-1] + nums[i])
        
        ans = [-1] * k

        for i in range(k, len(nums)-k):
            if i - k == 0:
                ans.append((prefix[i+k])//(2*k+1))
            else:
                ans.append((prefix[i+k]-prefix[i-k-1])//(2*k+1))
            
        for i in range(k):
            ans.append(-1)
        return ans


