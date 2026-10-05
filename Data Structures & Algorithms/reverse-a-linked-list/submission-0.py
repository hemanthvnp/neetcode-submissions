# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        curr = head
        prev = None
        next = head
        while curr:
            next = next.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        