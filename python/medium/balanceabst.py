class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        res = None

        def dfs(root):
            if root:
                dfs(root.left)
                arr.append(root)
                dfs(root.right)

        dfs(root)

        def make(l, h):
            if l > h:
                return None
            m = int((l+h) / 2)
            ret = arr[m]
            ret.left = make(l, m-1)
            ret.right = make(m+1, h)
            return ret

        res = make(0, len(arr) - 1)
        return res