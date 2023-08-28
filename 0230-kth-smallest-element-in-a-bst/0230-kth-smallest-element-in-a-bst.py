# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
#dfs on the tree, append each node.val to an empty list
# sort the list
# take the kth index

        res = []
        stack = deque([root])
        while stack: 
            current = stack.popleft()
            res.append(current.val)
        
            if current.left: 
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            
        result = sorted(res)
        return result[k-1]