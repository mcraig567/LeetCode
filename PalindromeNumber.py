'''
Link: https://leetcode.com/problems/palindrome-number/
Topic: Algorithms
Difficulty: Easy
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:      
        if x == 0:
            return True
        
        if x < 0 or x % 10 == 0:
            return False
        
        newInt = 0
        while x > newInt:
            x, remainder = divmod(x, 10)
            newInt = newInt * 10 + remainder

        if newInt == x or newInt//10 == x:
            return True
        else:
            return False
