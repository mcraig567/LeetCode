'''
Link: https://leetcode.com/problems/reverse-integer/
Topic: Algorithms
Difficulty: Easy
'''

class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        
        if x < 0:
            temp = x * -1
        else:
            temp = x
        
        for i in range(temp):
            temp, remainder = divmod(temp, 10)
            ans = ans * 10 + remainder
            if temp == 0:
                break
                
        if x < 0:
            ans = ans * -1
            
        if ans < (-2 ** 31) or ans > (2 ** 31 - 1):
            ans = 0
            
        return ans
