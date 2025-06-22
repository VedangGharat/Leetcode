class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotation(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        n = len(nums)
        k = k % n
        rotation(0, n-1)
        rotation(0, k-1)
        rotation(k, n-1)