# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        num = []
        addOne = False
        while (l1 or l2):
            number = ((l1.val if l1 else 0) + (l2.val if l2 else 0))
            number = (number + 1) if addOne else number
            if number >= 10:
                number =  number - 10
                addOne = True
            else:                
                addOne = False

            num.append(number)
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None

        if addOne: 
            num.append(1)

        return num
        


l1_1 = ListNode(1)
# l1_2 = ListNode(4)
# l1_3 = ListNode(3)
# l1_1.next = l1_2
# l1_2.next = l1_3

l2_1 = ListNode(9)
l2_2 = ListNode(9)
#l2_3 = ListNode(4)
l2_1.next = l2_2
#l2_2.next = l2_3

print(Solution().addTwoNumbers(l1_1, l2_1))      