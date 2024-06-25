class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        ans = [1] * n
        left = [1] * n
        right = [1] * n

        left[0] = nums[0]
        for i in range(1, n):
            left[i] *= (nums[i] * left[i-1])

        right[-1] = nums[-1] 
        for i in range(n-2, 0, -1):
            right[i] *= (nums[i] * right[i+1])

        ans[0] = right[1]
        ans[-1] = left[-2]
        for i in range(1, n-1):
            ans[i] *= left[i-1] * right[i+1]

        return ans


        