# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        res = []
        uniqueCheck = set()
        def traverse(root):
            if root: 
                traverse(root.left)
                res.append(root.val)
                traverse(root.right)
        
        traverse(root)
        for val in res: 
            uniqueCheck.add(val)
        print(res)
        print (uniqueCheck)
        
        return (res) == sorted(res) and len(res) == len(uniqueCheck)
            