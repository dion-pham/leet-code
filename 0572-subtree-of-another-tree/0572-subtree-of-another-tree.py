# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #traverse through the root tree
        #if you reach a node that is the root of the subtree, start helper funciton
            #helper function: checks that all value are the same
                #if helper function returns true, return true for outer function
        def isSameTree(tree1, tree2):
            if not tree1 and not tree2: 
                return True

            if tree1 and tree2 and tree1.val == tree2.val: 
                return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right,tree2.right)

            return False 
            
            
        
        if not subRoot: return True
        if not root and subRoot: return False
        
        
        if isSameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
    
 
        
        
    