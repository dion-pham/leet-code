# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative solution: dfs stack 
        
        if not root: return 0
        stack = deque([[root,1]])
        res = 0
        
        while stack: 
            current, level = stack.popleft()
            
            res = max(res,level)
            if current.left:
                stack.append([current.left, level+1])
            if current.right:
                stack.append([current.right, level+1])
        return res
        