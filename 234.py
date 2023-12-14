# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x_1 = ''
        while head:
            x_1 += str(head.val)
            head = head.next
        return x_1 == x_1[::-1]
