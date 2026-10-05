"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        s = {}
        k = head
        if not head:
            return head
        while k:
            s[k] = Node(k.val)
            k = k.next
        k = head
        while k:
            if k.next:
                s[k].next = s[k.next]
            k = k.next
        k = head
        while k:
            if k.random:
                s[k].random = s[k.random]
            k = k.next
        return s[head]