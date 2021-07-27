'''
Link: https://leetcode.com/problems/3sum-closest/
Topic: Algorithms
Difficulty: Medium
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 9999999 #Difference from target - start high
        total = 0
        nums.sort()
        
        #For each value in nums, check all combinations (while reducing options as possible)
        for i in range(len(nums)):
            left = i + 1 #All values to the left of i will have already been tried in each combination
            right = len(nums) - 1
            
            while left < right:
                temp = nums[left] + nums[i] + nums[right]                
                if diff > abs(target - temp):
                    diff = abs(target - temp)
                    total = temp
                    
                if diff == 0:
                    return total
                
                if temp > target: #This 3SUM was too big, so reduce the large side
                    right -= 1
                    
                if temp < target: #This was too small, increase the smallest number
                    left += 1
                    
        return total
                    