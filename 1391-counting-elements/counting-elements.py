# Vedang
class Solution:
    def countElements(self, arr: List[int]) -> int:
        hmap = collections.Counter(arr)
        count = 0
        for k, v in hmap.items():
            if k+1 in hmap:
                count += v
        return count
                
