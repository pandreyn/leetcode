"""
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 is None and l2 is None:
            return None
        
        minVal = 0
        if l2 is None or (l1 and l1.val < l2.val):
            minVal = l1.val
            l1 = l1.next
        else:
            minVal = l2.val
            l2 = l2.next
        
        head = l3 = ListNode(minVal)
        
        while l1 or l2:
            if l2 is None or (l1 and l1.val < l2.val):
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            
            l3 = l3.next

        return head


l11 = ListNode(1)
l12 = ListNode(2)
l13 = ListNode(4)
l11.next = l12
l12.next = l13

l21 = ListNode(1)
l22 = ListNode(3)
l23 = ListNode(4)
l21.next = l22
l22.next = l23
print(Solution().mergeTwoLists(l11, l21))
