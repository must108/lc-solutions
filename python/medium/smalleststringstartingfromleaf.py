class Solution:
    def dfs(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [chr(root.val + ord('a'))]

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        paths = []
        for path in left + right:
            if path:
                paths.append(path + chr(root.val + ord('a')))
        return paths

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        paths = self.dfs(root)
        return min(paths)