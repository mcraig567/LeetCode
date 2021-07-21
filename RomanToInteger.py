'''
Link: https://leetcode.com/problems/roman-to-integer/
Topic: Algorithms
Difficulty: Easy
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        letters = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        for i in range(len(s) - 2, -1, -1):
            if letters[s[i]] < letters[s[i+1]]:
                ans -= letters[s[i]]
            else:
                ans += letters[s[i]]
        
        ans += letters[s[len(s)-1]]
        
        return ans
