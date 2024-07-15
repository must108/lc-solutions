class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        res = []

        while q:
            l = len(q)
            level = []

            for i in range(l):
                n = q.pop(0)
                level.append(n.val)

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            res.append(level)
        
        return res