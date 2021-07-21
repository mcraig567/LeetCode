'''
Link: https://leetcode.com/problems/valid-parentheses/
Topic: Algorithms
Difficulty: Easy
'''

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(": ("normal", 1),
            ")": ("normal", -1),
            "[": ("square", 1),
            "]": ("square", -1),
            "{": ("curly", 1),
            "}": ("curly", -1)
        }
        
        bracketCount = {
            "normal": 0,
            "square": 0,
            "curly": 0            
        }
        
        #Keep track of what brackets are open
        recentOpen = []
        
        for char in s:
            bracketType = brackets[char][0]
            direction = brackets[char][1]
            
            #Check to see if open or closed bracket, ensure closing most recently opened bracket
            if direction == 1:
                recentOpen.append(bracketType)
            else:
                if len(recentOpen) == 0 or recentOpen.pop() != bracketType:
                    return False
                
            bracketCount[bracketType] += direction
        
        #If valid, all counts will be 0
        if bracketCount["normal"] == 0 and bracketCount["square"] == 0 and bracketCount["curly"] == 0:
            return True
        else:
            return False
