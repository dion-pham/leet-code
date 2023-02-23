# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
# start at the lower of the two roots. traverse down tree and keep a track of lowest.
    # 
        # lowest = float("inf")
        # queue = [root]
        # nodes = []
        # while queue: 
        #     current = queue.pop(0)
        #     if current.val < lowest: 
        #         lowest = current.val
        #     if current.val == q: 
        #         nodes.append(q)
        #     if current.val == p: 
        #         nodes.append(p)    
        #     if len(nodes) == 2: 
        #         return lowest
        #     if current.left is not None: 
        #         queue.append(current.left)
        #     if current.right is not None: 
        #         queue.append(current.right)
        # return lowest

        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root