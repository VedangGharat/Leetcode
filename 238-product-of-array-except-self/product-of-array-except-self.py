class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        product_left = 1
        product_right = 1
        for i in range(len(nums)-1):
            # left side
            product_left *= nums[i]
            ans[i+1] *= product_left
            
            #right side
            product_right *= nums[len(nums)-1-i]
            ans[len(nums)-2-i] *= product_right

        return ans
  
