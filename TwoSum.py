'''
Link: https://leetcode.com/problems/two-sum/
Topic: Algorithms
Difficulty: Easy
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existingNums = {}
        for i in range(len(nums)):        
            rem = target - nums[i]
            pair = existingNums.get(rem)
            
            if pair != None and pair != i:
                ans = [pair, i]
                return ans
            
            existingNums[nums[i]] = i
            
        return "No two sums in this array"
