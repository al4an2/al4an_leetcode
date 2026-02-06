
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        new_nodes = dict()

        def dfs(node):
            if node in new_nodes:
                return new_nodes[node]

            new_node = Node(val = node.val)
            new_nodes[node] = new_node
            for nb in node.neighbors:
                new_node.neighbors.append(dfs(nb))
            return new_node
                
        return dfs(node)