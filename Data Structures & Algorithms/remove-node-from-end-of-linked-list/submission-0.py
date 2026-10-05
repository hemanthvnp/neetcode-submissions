# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        s = head
        count = 0
        while s:
            s = s.next
            count+=1
        s = head
        if count==n:
            return head.next
        n1 = count-n-1
        while n1 and s:
            s = s.next
            n1-=1
        if s.next:
            s.next = s.next.next
        return head