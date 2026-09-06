"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(root: ListNode):
    r = root
    s = ""
    while r:
        s += f" -> {r.val}"
        r = r.next
    return s


def add_two_numbers_optimized(
    l1: ListNode | None, l2: ListNode | None
) -> ListNode | None:
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        # Obtain the current solution
        value1 = l1.val if l1 else 0
        value2 = l2.val if l2 else 0

        # Calculate the sum and update carry
        value = value1 + value2 + carry
        carry = value // 10

        # Attach the single digit result node
        current.next = ListNode(value % 10)
        current = current.next

        # Advance in the list
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    carry = 0
    # Approach of pointer for everyone and dummy node.
    top = l1
    bottom = l2
    dummy_node = ListNode(0)
    curr_ptr = dummy_node

    while top or bottom:
        value = carry
        carry = 0  # once we use it, delete in order to not execute the ectra loop
        if top and bottom:
            value = top.val + bottom.val + value
            top = top.next
            bottom = bottom.next

        # Only top left
        elif top:
            value = top.val + value
            top = top.next

        # Only bottom left
        else:
            value = bottom.val + value
            bottom = bottom.next

        # Obtain the new carry and value parsed
        if value >= 10:
            carry, value = divmod(value, 10)

        # Create new node and continue
        curr_ptr.next = ListNode(value)
        curr_ptr = curr_ptr.next

    # Lastly, if carry is there, add it too
    if carry != 0:
        curr_ptr.next = ListNode(carry)

    return dummy_node.next


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(f"First list: {print_list(l1)}")
    print(f"Second list: {print_list(l2)}")
    print(f"Result: {print_list(add_two_numbers(l1, l2))}")
    print(f"Result OPT: {print_list(add_two_numbers_optimized(l1, l2))}")

    l1 = ListNode(0)
    l2 = ListNode(0)
    print(f"\nFirst list: {print_list(l1)}")
    print(f"Second list: {print_list(l2)}")
    print(f"Result: {print_list(add_two_numbers(l1, l2))}")
    print(f"Result OPT: {print_list(add_two_numbers_optimized(l1, l2))}")

    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    print(f"\nFirst list: {print_list(l1)}")
    print(f"Second list: {print_list(l2)}")
    print(f"Result: {print_list(add_two_numbers(l1, l2))}")
    print(f"Result OPT: {print_list(add_two_numbers_optimized(l1, l2))}")
