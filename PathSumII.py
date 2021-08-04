'''
Link: https://leetcode.com/problems/path-sum-ii/
Topic: Algorithms
Difficulty: Medium
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        paths = []
		paths.append(recursivePath([], root, paths))
		paths.pop()
        
        ans = []
        for path in paths:
            sum = 0
            for item in path:
                sum += item
                    
            if sum == targetSum:
                ans.append(path)

        
        return ans
    
'''	Get all paths from root to leaf 
Returns a list of lists that go [root, middle, leaf]
Final item in list is nested lists - remove once complete
'''
def recursivePath(self, path, root: TreeNode, paths):   
	path.append(root.val)
	if not root.left and not root.right:
		paths.append(path)

	if root.left:
		newPath = copy.copy(path)
		recursivePath(newPath, root.left, paths)

	if root.right:
		newPath = copy.copy(path)
		recursivePath(newPath, root.right, paths)
		
	return paths
