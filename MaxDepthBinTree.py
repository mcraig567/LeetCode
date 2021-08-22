'''
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Topic: Algorithms
Difficulty: Easy
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.checkChildren(root, 0)
        
        
    def checkChildren(self, root, depth):
        #print("Checking node ", root.val, ". Depth: ", depth)
        left = 0
        right = 0
        depth += 1
        
        if root.left:
            left = self.checkChildren(root.left, depth)
        if root.right:
            right = self.checkChildren(root.right, depth)
            
        return max(left, right, depth)
