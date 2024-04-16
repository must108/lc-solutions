class Solution:
    def helper(self, root: Optional[TreeNode], currSum: int) -> int:
        if not root:
            return 0

        currSum = (currSum * 10) + root.val
        if not root.left and not root.right:
            return currSum
        return self.helper(root.left, currSum) + self.helper(root.right, currSum)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)