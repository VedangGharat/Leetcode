class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        l, r = 0, len(nums)-1
        i = len(nums)-1
        while i >=0 and l <= r:
            if abs(nums[l]) < abs(nums[r]):
                square = nums[r]
                r -= 1
            else: 
                square = nums[l]
                l += 1
            
            arr[i] = square * square
            i -= 1
        return arr