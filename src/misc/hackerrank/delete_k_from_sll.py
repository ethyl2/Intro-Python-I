"""
https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm

Solve in O(n) time using O(1) additional space

given sll of integers l and int k, remove all els from l that have value == k
Return l

"""


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def remove_from_list(l, k):
    # Deal with edge cases first
    if l == None:
        return l

    # This deals with an example like l=[1000, 1000], k = 1000, so should return []
    while l.value == k:
        if l.next:
            l = l.next
        else:
            l = None
            return l

    # Loop through until the curr.next is k or there is no curr.next
    curr = l
    while curr.next and curr.next.value != k:
        curr = curr.next

    # If curr.next's value is k, skip over curr.next by reassigning curr.next pointer
    if curr.next and curr.next.value == k:
        curr.next = curr.next.next
    return l


node3 = ListNode(3)
node1 = ListNode(1)
node2 = ListNode(2)
node3_again = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node3.next = node1
node1.next = node2
node2.next = node3_again
node3_again.next = node4
node4.next = node5

# [3,1,2,3,4,5] -> [1,2,4,5]
print(remove_from_list(node3, 3).value)
# looks like it is getting the tail b/c adding a next. in here results in a nonetype error
print(remove_from_list(node1, 5).next.next.value)
