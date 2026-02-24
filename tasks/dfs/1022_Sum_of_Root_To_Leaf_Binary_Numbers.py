# Definition for a binary tree node.
from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = []

        def dfs(node, cur):
            if not node:
                return 0
            
            cur = (cur << 1) | node.val

            if not node.left and not node.right:
                result.append(cur)
            
            dfs(node.left, cur)
            dfs(node.right, cur)

        dfs(root, 0)
        return sum(result)