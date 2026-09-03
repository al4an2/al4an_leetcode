from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, c_sum):
            if node is None:
                return False
            
            if node.left is None and node.right is None and node.val + c_sum == targetSum:
                return True
            return dfs(node.left, node.val + c_sum) or dfs(node.right, node.val + c_sum)

        return dfs(root, 0)

#simple leetcode-style optimization
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        targetSum -= root.val
        if root.left is None and root.right is None and targetSum == 0:
            return True
            
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)