# reverse a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Brute force - nested loop - O(n^2), O(1)
## Iterative - O(n), O(1)
## Recursive - O(n), O(n) stack frame space


# Iterative
def reverseList(head: ListNode) -> ListNode:
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


# Recursive
def reverseList(head: ListNode) -> ListNode:
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = reverseList(head.next)
        head.next.next = head
    head.next = None

    return newHead
