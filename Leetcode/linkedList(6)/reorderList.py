# Reorder the nodes of a linked list into a given order
# 0 , n-1 , 1 , n-2 , 3 , n-3 , ...


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Brute force - put LL nodes into an array and rearrange pointers
#              - O(n), O(n)
## Recursively - can do it without an array but - O(n), O(n)
## Optimal - Find the middle, reverse the 2nd part of LL,
#            combine both the LLs - O(n), O(1)


def reorderList(head: [ListNode]) -> None:

    # finding middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    end_head = slow.next
    slow.next = None

    # reversing 2nd half
    curr = end_head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    # combining LLs
    head2 = prev
    head1 = head

    curr1 = head1
    curr2 = head2
    while curr2:
        temp1 = curr1.next
        temp2 = curr2.next
        curr1.next = curr2
        curr2.next = temp1
        curr1 = temp1
        curr2 = temp2
