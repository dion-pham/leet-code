# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
#         perform the recursive in order traversal for a BST
#         append items to a list
#         if list == list sorted, then it was a valid bst

        res = []
        uniqueVals = set()
        def traverse(root):
            if root: 
                traverse(root.left)
                res.append(root.val)
                traverse(root.right)
                
        traverse(root)
        for num in res: 
            uniqueVals.add(num)
        return res == sorted(res) and len(res) == len(uniqueVals)