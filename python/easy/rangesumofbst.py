class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        if root.val not in range(low, high + 1):
            return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

        print(root.val)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
