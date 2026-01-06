from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = 0
        max_on_level = float("-inf")
        result = -1

        while queue:
            level += 1
            level_sum = 0
            size = len(queue)

            for _ in range(size):
                obj = queue.popleft()
                level_sum += obj.val

                if obj.left:
                    queue.append(obj.left)
                if obj.right:
                    queue.append(obj.right)
            
            if level_sum > max_on_level:
                result = level
                max_on_level = level_sum
        
        return result