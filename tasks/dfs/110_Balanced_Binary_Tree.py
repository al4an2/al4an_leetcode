# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, h):
            if not node:
                return 0
            h_l = dfs(node.left, h)
            if h_l == -1:
                return -1

            h_r = dfs(node.right, h)
            if h_r == -1:
                return -1

            if abs(h_l - h_r) > 1:
                return -1

            return max(h_l, h_r) + 1
        
        return dfs(root, 0) != -1
