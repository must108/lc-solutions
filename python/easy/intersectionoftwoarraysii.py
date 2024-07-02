class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        short = nums1 if len(nums1) <= len(nums2) else nums2
        l = nums1 if len(nums1) > len(nums2) else nums2
        h = {}
        res = []

        for i in range(len(short)):
            h[short[i]] = 1 + h.get(short[i], 0)

        for i in range(len(l)):
            if l[i] in h:
                if h[l[i]] == 0:
                    h.pop(l[i])
                else:
                    h[l[i]] -= 1
                    res.append(l[i])

        return res