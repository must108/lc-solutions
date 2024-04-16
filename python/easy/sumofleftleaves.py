class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        sum1 = 0
        if root.left and not root.left.left and not root.left.right:
            sum1 += root.left.val

        sum1 += self.sumOfLeftLeaves(root.left)
        sum1 += self.sumOfLeftLeaves(root.right)

        return sum1