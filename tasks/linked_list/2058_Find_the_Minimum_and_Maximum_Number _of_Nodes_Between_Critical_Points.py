from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        node = head.next
        counter = 1

        min_dist = float('inf')
        first = None
        last = None

        while node.next is not None:
            if prev.val < node.val > node.next.val or prev.val > node.val < node.next.val:

                if first is None:
                    first = counter
                else:
                    min_dist = min(min_dist, counter - last)

                last = counter

            prev = node
            node = node.next
            counter += 1

        if first is not None and last != first:
            return [min_dist, last - first]

        return [-1, -1]
