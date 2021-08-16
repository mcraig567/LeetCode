'''
Link: https://leetcode.com/problems/symmetric-tree/
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return True and self.forwardTraverse(root, root)
            
    def forwardTraverse (self, left, right):       
        if not left and not right:
            return True 
        elif not left or not right:
            return False
        
        if left.val != right.val:
            return False
        
        leftTest = self.forwardTraverse(left.left, right.right)
        rightTest = self.forwardTraverse(left.right, right.left)
            
        return leftTest and rightTest