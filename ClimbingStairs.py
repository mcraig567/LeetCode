'''
Link: https://leetcode.com/problems/climbing-stairs/
Topic: Algorithms
Difficulty: Easy
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        #Each step can be reached by the step below it or the step two below it
        steps = {}
        steps[1] = 1 #One way to reach first step
        steps[2] = 2 #Two ways to reach second step
        
        for i in range(3, n+1):
            steps[i] = steps[i-1] + steps[i-2]
            
        return steps[n]
