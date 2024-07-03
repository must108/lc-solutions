class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        res = [0] * 4

        l = nums[:-3]
        m1 = nums[1:-2]
        m2 = nums[2:-1]
        s = nums[3:]

        if l:
            res[0] = l[-1] - l[0]
        if m1:
            res[1] = m1[-1] - m1[0]
        if m2:
            res[2] = m2[-1] - m2[0]
        if s:
            res[3] = s[-1] - s[0]

        return min(res) if res else 0