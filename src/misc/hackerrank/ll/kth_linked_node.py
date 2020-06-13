"""
Hackerrank test #1
Given head of ll
and int k

Remove the kth node from the end of a linked list and return the head

If k > len(ll)  return head without modifying anything

Optimal is O(n) runtime and O(1) space.
"""


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthLinkedListNode(head, k):
    # edge cases
    if head is None:
        return None

    # Determine length of ll
    length = 1
    curr = head
    while curr.next:
        length += 1
        curr = curr.next
    # print(length)

    # If k > length:
    # return head
    if k > length:
        print("k > length")
        return head

    # If k == length, return the next node
    if k == length:
        return head.next

    # Progress until length - k - 1 This will get us to the node before the kth node from end.
    distance = length - k - 1
    # Reset curr
    curr = head
    while distance > 0:
        curr = curr.next
        distance -= 1
    # Reassign next pointers to skip over kth node
    curr.next = curr.next.next

    return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
print(removeKthLinkedListNode(node1, 2).value)


def print_ll(head):
    ll_list = []
    curr = head
    while curr is not None:
        ll_list.append(curr.value)
        curr = curr.next
    print(ll_list)
    return ll_list


print_ll(node1)
