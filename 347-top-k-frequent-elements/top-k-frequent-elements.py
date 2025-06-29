class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hmap = {}
        for i in nums:
            count_hmap[i] = count_hmap.get(i, 0) + 1

        freq = [[] for i in range(len(nums)+1)]

        for ke, v in count_hmap.items():
            freq[v].append(ke)

        res = []
        for val_range in range(len(freq)-1, -1, -1):
            for val in freq[val_range]:
                res.append(val)
                if len(res) == k:
                    return res

