# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        
        
        
# note; in a BST, all the elements are sorted. 
# traverse the tree, keep track of node values
    # append to a list
    # find the kth smallest value according to that list
# ^^ the method above can be implemented using recursion: DFS with inorder traversal 

        res =[]

        def traverse(root):
            if root: 
                traverse(root.left)
                res.append(root.val)
                traverse(root.right)

        traverse(root)
        return res[k-1]


