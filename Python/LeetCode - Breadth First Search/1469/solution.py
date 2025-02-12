# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        lonely = []

        while queue:
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
                if not node.right:
                    lonely.append(node.left.val)

            if node.right:
                queue.append(node.right)
                if not node.left:
                    lonely.append(node.right.val)
        
        return lonely
