# Check if the LL has a cycle
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Hashmap - loop through checking hashmap - O(n), O(n)
## Fast+Slow pointer - loop till end, if fast and slow meet x_X
##                   - O(n), O(1)

## reason why it is O(n) - the fast and slow pointer have gap between them
## that reduces by 1 every step, the max length the gap can be is n


def hasCycle(self, head: [ListNode]) -> bool:
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
