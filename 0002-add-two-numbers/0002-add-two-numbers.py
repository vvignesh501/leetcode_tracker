# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        output = ListNode(-1)
        temp = output
        while l1 or l2 or carry:

            if l1:
                add1 = l1.val
                l1 = l1.next
            else:
                add1 = 0

            if l2:
                add2 = l2.val
                l2 = l2.next
            else:
                add2 = 0
            
            add = (add1 + add2 + carry)
            rem = add % 10
            carry = add // 10

            newNode = ListNode(rem)
            temp.next = newNode
            temp = temp.next
        
        return output.next



# Time complexity = O(n)
# Space complexity = O(1)
            