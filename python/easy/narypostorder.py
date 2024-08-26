class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []

        def narypost(root):
            if root:
                for node in root.children:
                    narypost(node)
                ret.append(root.val)

        narypost(root)
        return ret