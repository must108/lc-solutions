class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        rt = []
        ret = []
        
        for i in range(len(nums)):
            t = str(nums[i])

            res = ""
            for c in t:
                res += str(mapping[int(c)])

            rt.append([int(res), i])

        rt.sort()
        for p in rt:
            ret.append(nums[p[1]])

        return ret