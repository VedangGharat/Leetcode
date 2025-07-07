class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {"]":"[", ")":"(", "}":"{"}
        stack = []
        for p in s:
            if p in hmap.values():
                stack.append(p)
            elif stack and stack[-1] == hmap[p]:
                stack.pop()
            else: return False
        return stack == []