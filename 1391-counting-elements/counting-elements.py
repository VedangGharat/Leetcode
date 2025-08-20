# Vedang
class Solution:
    def countElements(self, arr: List[int]) -> int:
        hmap = collections.Counter(arr)
            
        return sum(v for k, v in hmap.items() if k+1 in hmap)
                
