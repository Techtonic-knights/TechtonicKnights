# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def bfs(root, target):
            queue = deque([root])
            while queue:
                node = queue.popleft()
                
                if node.val == target.val:
                    return node

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            return None 

        return bfs(cloned, target)

