class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = {}
        n = len(nums)

        for i in range(n):
            num = target - nums[i]
            if num in ret:
                return [ret[num], i]
            ret[nums[i]] = i        

        return []