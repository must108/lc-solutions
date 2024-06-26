class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                t = nums[i+1]
                nums[i+1] = nums[i] + 1
                count += 1 + nums[i] - t

        return count
        
