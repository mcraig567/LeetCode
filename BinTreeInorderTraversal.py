'''
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:        
        ans = []
        if not root:
            return ans
		
        if root.left:
            print("left")
            ans.extend(self.inorderTraversal(root.left))
            
        ans.append(root.val)
        
        if root.right:
            print("right")
            ans.extend(self.inorderTraversal(root.right))

        return ans
