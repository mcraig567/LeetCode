'''
Link: https://leetcode.com/problems/merge-sorted-array/
Topic: Algorithms
Difficulty: Easy
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        #Start from high end so easier to replace 0s
        ind1 = m - 1
        ind2 = n - 1
        addInd = m + n - 1
        
        #This will move all existing nums1 to the right, but not fill nums1 up if ind1 finishes before ind2
        while ind1 >= 0 and ind2 >= 0:
            if nums1[ind1] > nums2[ind2]:
                nums1[addInd] = nums1[ind1]
                ind1 -= 1
            else:
                nums1[addInd] = nums2[ind2]
                ind2 -= 1

            addInd -= 1
            
        #Catch any items in nums2 that need to get added to the start of nums1
        while ind2 >= 0:
            nums1[ind2] = nums2[ind2]
            ind2 -= 1
