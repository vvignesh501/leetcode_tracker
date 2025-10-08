class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tail = head
        while tail and tail.next:
            head = head.next
            tail = tail.next.next
        return head