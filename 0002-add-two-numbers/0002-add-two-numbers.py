# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a new list Node
        l3 = ListNode(-1)
        temp = l3
        carry = 0

        while l1 or l2 or carry:  

            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0

            add = val1 + val2 + carry
            rem = add % 10
            carry = add // 10

            temp.next = ListNode(rem)
            temp = temp.next
        
        return l3.next


# Time complexity = O(n)
# Space complexity = O(1)
            