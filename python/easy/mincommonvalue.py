class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s = nums1 if len(nums1) <= len(nums2) else nums2
        l = nums1 if len(nums1) > len(nums2) else nums2
        sp = 0
        lp = 0

        while(sp < len(s) and lp < len(l)):
            if l[lp] == s[sp]:
                return s[sp]
            elif l[lp] > s[sp]:
                sp += 1
            elif l[lp] < s[sp]:
                lp += 1

        return -1