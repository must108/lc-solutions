"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret = []

        def narypre(root):
            if root:
                ret.append(root.val)
                for node in root.children:
                    narypre(node)

        narypre(root)
        return ret