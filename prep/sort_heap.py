"""
Heap Sort
-----------
Works by visualizing the elements of an array as a special kind of
complete binary tree called a heap.

A complete binary tree has an interesting property that we can use to
find the children and parents of any node.

If the index of any element in the array is `i`, the element in the
index `2i+1` will become the left child and the element in `2i+2` index
will become the right child. Also, the parent of any element at index
`i` is given by the lower bound of (i-1)/2

Heap is a special tree-based data structure. A binary tree is said to
follow a heap data structure if
  - it is a complete binary tree
  - All nodes in the tree follow the property that they are greater than
    their children and smaller than the root and so on. Such a heap is
    called a max-heap. If instead, all nodes are smaller than their
    children, it is called a min-heap.

Starting from a complete binary tree, we can modify it to become a
max-heap by running a function called "heapify" on all the non-leaf
elements of the heap. This will involve recursion. This can be done by
swapping the nodes until a tree structure satisfies the max-heap
definition.

To build a max-heap from any tree, we can start heapifying each sub-tree
from the bottom up and end up with a max-heap after the function is
applied to all elements including the root element.

In case of a complete tree, the first index of a non-leaf is given by
`n/2 - 1`. All other nodes after that are leaf-nodes and don't need to
be heapified.

Example:
    [1, 12, 9, 5, 6, 10]
    n = 6 -> n/2 - 1 = 2
    build from bottom up so loop from 2 to 0.

Start by heapifying the lowest smallest trees and gradually move up
unitl we reach the root element.

Breakdown:
1. Since the tree satisfies Max-Heap Property, then the largest item
   is stored at the root node.
2. Swap: Remove the root element and put at the end of the array (nth
   position). Put the last item of the tree (heap) at the vacant place.
3. Remove: Reduce the size of the heap by 1
4. Heapify: Heapify the root element again so that we have the highest
   element at root.
5. The process is repeated until all the items of the list are sorted.

Runtime: O(n*log(n))
Memory: O(1)
"""


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build max heap
    # for in in reversed(range(0, (n//2)+1))
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    # for i in reversed(range(1,n))
    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)
