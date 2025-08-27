class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # tail of the processed list

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # swap
            prev.next = second
            first.next = second.next
            second.next = first

            # move prev pointer 2 nodes forward
            prev = first

        return dummy.next
