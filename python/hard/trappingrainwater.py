class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ret = 0

        n = len(height)
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                pHeight = height[stack[-1]]
                stack.pop()

                if not stack:
                    break

                dist = i - stack[-1] - 1
                minHeight = min(height[stack[-1]], height[i]) - pHeight
                ret += dist * minHeight

            stack.append(i)

        return ret