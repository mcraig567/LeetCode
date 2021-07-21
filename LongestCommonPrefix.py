'''
Link: https://leetcode.com/problems/longest-common-prefix/
Topic: Algorithms
Difficulty: Easy
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixLength = len(strs[0])
        prefix = strs[0]
        for word in strs[1:]:
            if len(word) < prefixLength:
                prefixLength = len(word)              
            for i in range(prefixLength-1, -1, -1):
                if word[i] != prefix[i]:
                    prefixLength = i        
        return prefix[:prefixLength]
