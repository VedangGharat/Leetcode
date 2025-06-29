class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tracking = []
        for i in nums1:
            if i in nums2:
                tracking.append(i)
                # nums2.remove(i)
        return list(set(tracking))