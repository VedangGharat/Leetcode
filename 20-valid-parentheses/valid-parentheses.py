class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {")":"(", "]":"[", "}":"{"}
        stack = []
        for p in s:
            if p in hashMap.values():
                stack.append(p)
            elif stack and stack[-1] == hashMap[p]:
                stack.pop()
            else:
                return False
        return stack == []