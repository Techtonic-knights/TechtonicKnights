# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        parent_x, parent_y = None, None
        level_x, level_y = -1, -1
        
        queue = deque([(root, None, 0)])
        
        while queue:
            node, parent, level = queue.popleft()
            
            if node.val == x:
                parent_x, level_x = parent, level
            if node.val == y:
                parent_y, level_y = parent, level
            
            if parent_x is not None and parent_y is not None:
                break
            
            if node.left:
                queue.append((node.left, node, level + 1))
            if node.right:
                queue.append((node.right, node, level + 1))
        
        return level_x == level_y and parent_x != parent_y
