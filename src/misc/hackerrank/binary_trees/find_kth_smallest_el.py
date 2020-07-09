"""
From Kapil Sharma's lecture 07-09-2020
Find the kth smallest element from an array.

Example:
A = [2,7,1,5,3,8,4]
k = 2
Return 2

A [25,10,20,15,5]
k = 3
Return 15

My first instinct is to sort the array and then find array[k-1].
This would work as long as there are no duplicates.
    In order to work with duplicates, add this line of code at the top of the function:
        arr = list(set(arr))
    
Time complexity: O(n log n) for timsort + O(1) for access == O(n log n)
Space complexity: O(1)
"""


from heapq import heapify, heappush, heappop


def find_kth_smallest_el(arr, k):
    arr = list(set(arr))
    if arr == None or k == None or k > len(arr) or len(arr) == 0 or k == 0:
        return None
    arr.sort()
    return arr[k-1]


print(find_kth_smallest_el([2, 5, 1], 4))
print(find_kth_smallest_el([2, 7, 1, 5, 3, 8, 4], 2))
print(find_kth_smallest_el([25, 10, 20, 15, 5], 3))

# Add duplicate fix before running this one:
# print(find_kth_smallest_el([3, 3, 3, 5], 2))

'''
Kapil suggested using a min heap.
Python has a handy heapq class, which is a min heap by default. Nice!

Again, this works as long as there are no duplicates.
    In order to work with duplicates, add this line of code at the top of the function:
        arr = list(set(arr))

'''


def find_kth_smallest_el_with_min_heap(arr, k):

    if arr == None or k == None or k > len(arr) or len(arr) == 0 or k == 0:
        return None
    min_heap = []
    heapify(min_heap)

    for i in range(len(arr)):
        heappush(min_heap, arr[i])

    for i in range(k-1):
        heappop(min_heap)

    return min_heap[0]


print(find_kth_smallest_el_with_min_heap([2, 7, 1, 5, 3, 8, 4], 2))
print(find_kth_smallest_el_with_min_heap([25, 10, 20, 15, 5], 3))

# Add the duplicate fix and then you can run:
# print(find_kth_smallest_el_with_min_heap([2, 2, 3], 2))
