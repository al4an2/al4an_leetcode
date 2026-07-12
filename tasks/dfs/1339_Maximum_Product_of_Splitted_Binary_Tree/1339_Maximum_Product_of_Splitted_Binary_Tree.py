from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9+7
        all_sums = []

        def dfs(node):
            current = 0
            if node.left:
                left = dfs(node.left)
                current += left
            if node.right:
                right = dfs(node.right)
                current += right
            current = current + node.val
            all_sums.append(current)

            return current

        total_value = dfs(root)
        max_product = max((total_value - subtree_value) * subtree_value for subtree_value in all_sums)
        return max_product % MOD