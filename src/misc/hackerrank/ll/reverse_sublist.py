"""
From Sean Chen's code challenge lecture 10 Jun 2020

Given a sll, and 2 positions p & q, reverse the sublist between p & q.
Return the sll.

1 -> 2 -> 3 -> 4 -> 5
p = 2, q = 4
Return
1 -> 4 -> 3 -> 2 -> 5
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# One approach uses a stack to put values of nodes p thru q in, and then
# traverses the sll a second time from p to q, popping values off of the stack
# and setting the nodes to be those values.
# Time complexity would be O(2n + m), where n = q-p and  m = p - 1 (which is the length of the ll from the head to p)
# Space complexity: O(n)


def reverse_sublist(head, p, q):
    curr = head
    index = 1
    stack = []
    sublist_head = None
    while curr and index <= q:
        if curr.value == p:
            sublist_head = curr
            stack.append(curr.value)
        elif curr.value > p and index <= q:
            stack.append(curr.value)
        index += 1
        curr = curr.next

    curr = sublist_head
    while curr and len(stack) > 0:
        curr.value = stack.pop()
        curr = curr.next

    return head

# A more efficient way would be to do this function in one pass of the sll.


def reverse_sublist_in_place(head, p, q):
    curr = head
    index = 1
    while curr and index < p - 1:
        curr = curr.next
        index += 1
    (sub_head, sub_tail, next_node) = reverse(curr.next, q-p)
    curr.next = sub_head
    sub_tail.next = next_node
    return head


def reverse(head, num_places):
    prev = head
    curr = head.next
    index = 1
    while curr and index <= num_places:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        index += 1
    return(prev, head, curr)


# ---------------------------
# Testing it out

def ll_to_list(head):
    output_list = []
    curr = head
    while curr:
        output_list.append(curr.value)
        curr = curr.next
    return(output_list)


def print_before_and_after_reverse_sublist(head, p, q, reverse_function):
    print("Before: " + str(ll_to_list(head)))
    reverse_function(head, p, q)
    print("After: " + str(ll_to_list(head)))

# 1 -> 2 -> 3 -> 4 -> 5


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print_before_and_after_reverse_sublist(node1, 2, 4, reverse_sublist)
print('\n')
print_before_and_after_reverse_sublist(node1, 2, 4, reverse_sublist_in_place)
