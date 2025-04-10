from checker import Checker
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        carry //= 10
        current.next = ListNode(carry % 10)
        current = current.next
    return dummy.next


if __name__ == "__main__":
    checker = Checker(__file__)
    checker.check(add_two_numbers)
