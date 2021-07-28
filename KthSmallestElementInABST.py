# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        output = []
        def dfs(root):
            
            if not root:
                return
            
            if len(output) == k:
                return
            
            dfs(root.left)
            output.append(root.val)
            dfs(root.right)
            
        dfs(root)
        
        return output[k-1]
        
        