# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            
            # No need to create a new List Node, reuse the existing Node list1
            if list1.val < list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next

        while list1:
            tail.next = list1
            list1 = list1.next
            tail = tail.next

        while list2:
            tail.next = list2
            list2 = list2.next
            tail = tail.next
        
        return dummy.next

# Time = O(n)
# Space = why O(1) instead of O(n)
# No new nodes are created.
# You just relink existing nodes.
# At the end, the merged list is literally just the original list1 and list2 nodes rearranged.
# Only extra space used = the dummy head (constant).
# Space complexity = O(1)
        