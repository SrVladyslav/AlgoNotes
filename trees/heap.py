# Heap vs List
#
# +--------------------------------------+----------------------+----------------------+
# | Operation                            | List                 | Heap (heapq)         |
# +--------------------------------------+----------------------+----------------------+
# | Append / insert                      | O(1) amortized       | O(log n)             |
# | Access by index                      | O(1)                 | O(1)                 |
# | Find minimum                         | O(n)                 | O(1) -> heap[0]      |
# | Remove minimum                       | O(n)                 | O(log n)             |
# | Maintain priority automatically      | No                   | Yes                  |
# | Keep all elements fully sorted       | No                   | No                   |
# +--------------------------------------+----------------------+----------------------+
#
# Use a list when you need a general-purpose sequence.
# Use a heap when you frequently need to insert elements
# and retrieve/remove the smallest (or highest-priority) element efficiently.
#
# Note:
# heapq uses a regular Python list internally.
# It simply maintains the heap property on top of that list.


import heapq

heap: heapq = []

# Insert into the heap
value: tuple[int, int] = (1, 2)
heapq.heappush(heap, value)

print(type(heap))  # This is a list of tuples, heap doe snot change the type

print(f"The value of the heap is: {heap}")

# Extract the elements from the heap
while heap:
    smallest: tuple[int, int] = heapq.headpop(heap)
    print(f"The smallest element is: {smallest}")


# The normal list searches for the min in O(n) while the heap always has the minimum in O(1), since is the first element
l: list[int] = [6, 4, 5, 2, 3, 1]

# Transform to heap
hepq.heapify(l)
print(f"Min element from the list is: {l[0]}")
