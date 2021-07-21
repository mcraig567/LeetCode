'''
Link: https://leetcode.com/problems/custom-sort-string/
Topic: Algorithms
Difficulty: Medium
'''

class Solution:
    def customSortString(self, order: str, str: str) -> str:
        order_dict = {}
        letter_dict = {}
        for i in range(len(order)):
            order_dict[i] = order[i]
            letter_dict[order[i]] = True
         
        #Get number of each letter in str
        letters = {}
        ans = ''
        for i in range(len(str)):
            if not letter_dict.get(str[i]):
                ans = "".join((ans, str[i]))
            else:
                cur_amount = letters.get(str[i], 0)
                letters[str[i]] = cur_amount + 1
                

        for i in range(len(order_dict)):
            letter = order_dict[i]
            reps = letters.get(letter, 0)
            
            for i in range(reps):
                ans = "".join((ans, letter))
                
        return ans
