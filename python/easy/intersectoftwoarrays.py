class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = nums1 if len(nums1) <= len(nums2) else nums2
        l = nums1 if len(nums1) > len(nums2) else nums2
        res = []
        h = {}

        for i in range(len(s)):
            h[s[i]] = 1 + h.get(s[i], 0)

        for i in range(len(l)):
            if l[i] in h:
                if l[i] in res:
                    continue
                if h[l[i]] == 0:
                    h.pop(l[i])
                else:
                    h[l[i]] -= 1
                    res.append(l[i])

        return res