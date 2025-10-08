# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head

        # tail.next = the end of the array. Tht's why tail.next check is needed.
        # So that the program ends and when it's the end.
        
        while tail and tail.next:
            head = head.next
            tail = tail.next.next
        return head 
        
        