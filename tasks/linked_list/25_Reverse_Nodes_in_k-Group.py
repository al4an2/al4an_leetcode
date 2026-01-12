from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy_head = ListNode(next=head)
        prev_group = dummy_head
        curr = head

        while True:
           
            end = curr
            count = 0
            while count < k and end is not None:
                end = end.next
                count += 1

            if count < k:
                break 

            prev = None
            node = curr
            for _ in range(k):
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt

            prev_group.next = prev
            curr.next = end

            prev_group = curr
            curr = end

        return dummy_head.next