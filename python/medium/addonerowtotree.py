class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return None

        if depth == 1:
            temp = TreeNode(val)
            temp.left = root
            return temp

        if depth == 2:
            left = TreeNode(val)
            right = TreeNode(val)

            right.right = root.right
            right.left = None
            left.left = root.left
            left.right = None

            root.right = right
            root.left = left

            return root

        self.addOneRow(root.left, val, depth - 1)
        self.addOneRow(root.right, val, depth - 1)

        return root