# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
#   perform a bfs and keep track of level
#   maybe make use of a hash map to track by level
        # {1:[3], 2:[9,20]} --> list(object.values) in order to get the desired output
# from collections import deque    
        if root is None: 
            return []
        levels = []    
        queue = deque([(root,0)]) 
        
        while queue: 
            current,level_num = queue.popleft()
            #add to a sublist to append to output res list
            if len(levels) == level_num: 
                levels.append([current.val])
#           covers for 20 node when len(levels) != level_num
            else:
                levels[level_num].append(current.val)
    
            if current.left: 
                queue.append((current.left, level_num+1))
                
            if current.right: 
                queue.append((current.right, level_num+1))
                
        return levels
            
