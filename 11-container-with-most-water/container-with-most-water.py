class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_water = 0
        while l <= r:
            water = (r-l) * min(height[l], height[r])
            max_water = max(water, max_water)
            if height[l] >= height[r]:
                r-=1
            elif height[l] <= height[r]:
                l+=1
        return max_water