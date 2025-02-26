# Merge k different sorted linked lists - total n nodes


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Brute force - put all nodes in an array, sort - O(n. log n), O(n)
## Iterate each list for element - O(n. k), O(1)
## Merge sorts merging - O(n. log k), O(k)


# Iterative
def mergeKLists(lists: [[ListNode]]) -> [ListNode]:
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeList(l1, l2))
        lists = mergedLists
    return lists[0]


def mergeList(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next


# Recursive - O(log k)
def mergeKLists(lists):
    if not lists or len(lists) == 0:
        return None
    return divide(lists, 0, len(lists) - 1)


def divide(lists, l, r):
    if l > r:
        return None
    if l == r:
        return lists[l]
    mid = l + (r - l) // 2
    left = divide(lists, l, mid)
    right = divide(lists, mid + 1, r)
    return conquer(left, right)


def conquer(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1:
        curr.next = l1
    else:
        curr.next = l2
    return dummy.next
