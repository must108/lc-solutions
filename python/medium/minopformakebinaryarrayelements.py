class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                count += 1

        for i in range(len(nums)):
            if nums[i] == 0:
                return -1
        return count