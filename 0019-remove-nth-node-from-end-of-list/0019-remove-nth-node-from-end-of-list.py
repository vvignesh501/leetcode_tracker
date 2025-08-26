# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        total = 0
        while temp:
            temp = temp.next
            total += 1

        if n == total:
            return head.next # returns None -> [1] = 1.next = None

        # Move the node until one node before 3 in [1, 2, 3, 4, 5]
        prev = head
        for i in range(total - n - 1):
            prev = prev.next
        

        prev.next = prev.next.next
        return head

        