"""
Link: https://leetcode.com/problems/push-dominoes/
Topic: Algorithms
Difficulty: Medium
"""

"""
Initial Solution - O(N^2)
"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        This solution checks every domino whenever one falls over (creating a new state). At best it is O(N) if           there are no changes, and each domino is only checked once. At worst (edge domino falls over, and all             dominoes fall in that direction one at a time), it is O(N^2)
        """
        
        copy = dominoes
        change = True
        
        #Repeat until no more changes from initial to end state
        while change:
            dominoes = copy
            change = False
            
            if len(dominoes) == 0 | 1:
                return dominoes
            
            #Check edges - won't affect any additional dominoes so change is effectively false
            if dominoes[0] == '.' and dominoes[1] == "L":
                copy = ''.join(("L",copy[1:]))
            
            if dominoes[len(dominoes) - 1] == "." and dominoes[len(dominoes) - 2] == "R":
                copy = ''.join((copy[:len(dominoes) - 1], "R"))
            
            #Check for any standing dominoes that may get knocked over
            for i in range(1, len(dominoes) - 1):
                #print("Character:  ", dominoes[i], " - ", i)
                if dominoes[i] == '.':
                    if dominoes[i - 1] == "R" and dominoes[i + 1] == "L":
                        pass
                    elif dominoes[i - 1] == "R":
                        copy = ''.join((copy[:i], "R", copy[i+1:]))
                        change = True
                    elif dominoes[i + 1] == "L":
                        copy = ''.join((copy[:i], "L", copy[i+1:]))
                        change = True
        
        return copy

"""
Second Solution - O(N)
"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:        
        if len(dominoes) == 0|1:
            return dominoes
        
        #First iterate left to right across dominoes to see what dominoes fall to the right
        right = []
        falling = False
        for i in range(len(dominoes)):
            if dominoes[i] == "R":
                right.append(0)
                turns = 1
                falling = True
                
            elif dominoes[i] == "L":
                falling = False
                right.append(0)
                
            elif falling and dominoes[i] == ".":
                right.append(turns)
                turns += 1
                
            else:
                right.append(0)
                
        #Then iterate right to left, to see what dominoes fall to the left
        left = []
        falling = False
        for i in range(len(dominoes) - 1, -1, -1):
            if dominoes[i] == "L":
                left.append(0)
                turns = 1
                falling = True
                
            elif dominoes[i] == "R":
                left.append(0)
                falling = False
                
            elif falling and dominoes[i] == ".":
                left.append(turns)
                turns += 1
                
            else:
                left.append(0)
                
        #Left currently has last distance fist, need to reverse - O(N)
        left.reverse()
        
        #Compare left vs right to get direction of each domino
        ans = []
        
        for i in range(len(left)):
            if right[i] == 0 and left[i] == 0:
                ans.append(dominoes[i])
            elif right[i] > 0 and left[i] == 0: #indicates a "." that L couldn't reach (If "L", right would be 0)
                ans.append("R")    
            elif left[i] > 0 and right[i] == 0: #indicates a "." that R couldn't reach (If "R", left would be 0)
                ans.append("L")
            elif right[i] == left[i]: #indicates a "." tile that's evenly balanced
                ans.append(".")
            else:
                if right[i] > left[i]:
                    ans.append("L")
                else:
                    ans.append("R")
                
        ans = ''.join(ans)
        return ans
        

"""
Third Solution - combined forwards and backwords iterations
"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:        
        if len(dominoes) == 0|1:
            return dominoes
        
        #First iterate left to right across dominoes to see what dominoes fall to the right
        right = []
        left = []
        fallingRight = False
        fallingLeft = False
        for i in range(len(dominoes)):
            if dominoes[i] == "R":
                right.append(0)
                turnsRight = 1
                fallingRight = True
                
            elif dominoes[i] == "L":
                fallingRight = False
                right.append(0)
                
            elif fallingRight and dominoes[i] == ".":
                right.append(turnsRight)
                turnsRight += 1
                
            else:
                right.append(0)
                
            #Get dominoes falling to the left in the same iteration
            iterLeft = len(dominoes) - 1 - i
            if dominoes[iterLeft] == "L":
                left.append(0)
                turnsLeft = 1
                fallingLeft = True
                
            elif dominoes[iterLeft] == "R":
                left.append(0)
                fallingLeft = False
                
            elif fallingLeft and dominoes[iterLeft] == ".":
                left.append(turnsLeft)
                turnsLeft += 1
                
            else:
                left.append(0)
                
        #Left currently has last distance fist, need to reverse - O(N)
        left.reverse()
        
        #Compare left vs right to get direction of each domino
        ans = []
        
        for i in range(len(left)):
            if right[i] == 0 and left[i] == 0:
                ans.append(dominoes[i])
            elif right[i] > 0 and left[i] == 0: #indicates a "." that L couldn't reach (If "L", right would be 0)
                ans.append("R")    
            elif left[i] > 0 and right[i] == 0: #indicates a "." that R couldn't reach (If "R", left would be 0)
                ans.append("L")
            elif right[i] == left[i]: #indicates a "." tile that's evenly balanced
                ans.append(".")
            else:
                if right[i] > left[i]:
                    ans.append("L")
                else:
                    ans.append("R")
                
        ans = ''.join(ans)
        return ans
        