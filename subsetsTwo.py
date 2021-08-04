'''
Link: https://leetcode.com/problems/subsets-ii/
Topic: Algorithms
Difficulty: Medium
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in sorted(nums):		#Start with first number -- Answer accepts only if sorted
            temp = []
            for item in ans:			#Add number to end each list in ans
                temp += [item + [num]]
            ans += temp					#Add all the new lists to ans

        #Can't hash list of lists, need to make hashable - could maybe put in item loop above
        ans_dict = {}
        final_ans = []

        for item in ans:
            name = ""
            for char in item:
                name = name + str(char) #hashable string is characters in order [0,1,2] -> "012"
            if not ans_dict.get(name):	#Check if in dictionary, don't include in answer if already there
                ans_dict[name] = item
                final_ans.append(item)

        return final_ans