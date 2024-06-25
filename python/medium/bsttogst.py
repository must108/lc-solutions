class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0

        def dfs(root):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)

        dfs(root)
        return root