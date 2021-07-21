'''
Link: https://leetcode.com/problems/search-insert-position/
Topic: Algorithms
Difficulty: Easy
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        
        #Check bottom edge
        if target < nums[0]:
            return 0
        
        while high > low:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
             
        #Not in list - low == high
        if nums[high] < target:
            return high + 1
        else:
            return high
