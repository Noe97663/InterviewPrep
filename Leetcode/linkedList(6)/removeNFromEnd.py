# Remove the Nth node from the end of the LL


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Brute force - Loop twice - O(n), O(1)
## Recursively - O(n), O(n)
## 2 pointers- with a constant gap of N, when right node reaches end,
##             delete the node at the left pointer position,
##             dummy node for off by one error for left pointer.


def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next
