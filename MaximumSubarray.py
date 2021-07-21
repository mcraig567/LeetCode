'''
Link: https://leetcode.com/problems/maximum-subarray/
Topic: Algorithms
Difficulty: Easy
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:       
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
                
        return max(nums)
