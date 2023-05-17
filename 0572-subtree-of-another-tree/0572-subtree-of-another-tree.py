# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subRoot: 
            return True 
#        a null subtree is always a subtree of the root
        if not root: 
            return False 
#       a tree cannot be a subtree to a null root 
        if self.sameTree(root,subRoot):
            return True
        
#         call the original function recursively through DFS
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
        
        
    def sameTree(self,root,subRoot):
#        if both root and subroot are null, a null tree can have a null subtree
        if not root and not subRoot: 
            return True 
#        if both are non-null and the top level vals equal each other, perform a DFS to see if the rest of the tree is the same
        if root and subRoot and root.val == subRoot.val: 
            return self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right)
        
        return False 