class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums: 
            hmap[i] = hmap.get(i, 0) + 1

        elements = [ [] for i in range(len(nums)+1)]

        for key, value in hmap.items():
            elements[value].append(key)

        res = []
        for i in range(len(elements)-1, -1,-1):
            for e in elements[i]:
                res.append(e)
                if len(res) == k:
                    return (res)
