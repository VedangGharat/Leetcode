class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        occurance = 1
        p = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occurance += 1
            elif nums[i] != nums[i-1]:
                occurance = 1
            
            if occurance <=2:
                nums[p] = nums[i]
                p+=1
        return p
