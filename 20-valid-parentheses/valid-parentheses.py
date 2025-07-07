class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {")":"(", "]":"[", "}":"{"}
        res = []
        for c in s:
            if c in hmap.values():
                res.append(c)
            elif res and res[-1] == hmap[c]:
                
                res.pop()
            else:
                return False
        return res == []
