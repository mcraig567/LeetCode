'''
Link: https://leetcode.com/problems/find-peak-element/
Topic: Algorithms
Difficulty: Medium
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        index = (high - low) // 2
        
        if len(nums) == 1:
            return 0
        
        while high > low:                        
            #Check edges first
            if nums[0] > nums[1]:
                return 0
            
            elif nums[len(nums) - 1] > nums[len(nums) - 2]:
                return len(nums) - 1
            
            #Normal peak check
            elif nums[index] > nums[index - 1] and nums[index] > nums[index + 1]:
                return index
            
            #Check left hand side - if current larger, then must be larger on the right
            if nums[index] > nums[index - 1]:
                low = index
                index = low + (high - low) // 2
            else:
                high = index
                index = (high - low) // 2
