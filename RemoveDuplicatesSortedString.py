'''
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Topic: Algorithms
Difficulty: Easy
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        temp = ListNode()
        ans = temp
        
        temp.next = head
        
        #ans and temp both have a 0 at the beginning that causes problems if 0s at the
        #beginning of head. Check to see if beginning of head is 0, and skip temp up one if 
        #required
        if head.val == 0:
            temp = temp.next    
        
        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        else:
            return ans.next
