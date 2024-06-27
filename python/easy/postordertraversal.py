class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                ret.append(root.val)
        postorder(root)
        return ret