class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        l = 0
        maxVal = 0
        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1

            if (r - l + 1) - max(hmap.values()) <=  k:
                maxVal = max(maxVal, (r - l + 1))
            
            elif (r - l + 1) - max(hmap.values()) > k:
                hmap[s[l]] = hmap.get(s[l], 0) - 1
                l += 1
        
        return maxVal
