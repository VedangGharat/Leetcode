# Vedang
class Solution:
    def countElements(self, arr: List[int]) -> int:
        hmap = set(arr)
        count = 0
        for i in arr:
            if i+1 in hmap:
                count += 1 
        return count
