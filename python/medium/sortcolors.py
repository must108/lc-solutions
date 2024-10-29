class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = o = t = 0
        for num in nums:
            if num == 0:
                z += 1
            elif num == 1:
                o += 1
            elif num == 2:
                t += 1

        for i in range(z):
            nums[i] = 0

        for i in range(z, z+o):
            nums[i] = 1
        
        for i in range(z+o, z+o+t):
            nums[i] = 2