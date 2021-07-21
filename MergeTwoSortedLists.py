'''
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Topic: Algorithms
Difficulty: Easy
'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:       
        temp = ListNode() #Blank ListNode
        ans = temp #set ans to point at temp
        
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1  #Set next of temp to rest of l1
                l1 = l1.next    #Drop first element of l1 since now in temp
            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next    #Move temp up to most recently added element
            print()
            
        temp.next = l1 or l2    #Won't have last element as l1 or l2 will be None
        return ans.next         #ans points to beginning of temp still, will have entire list. 
                                #Need to remove the default 0 so move to first element of temp
        