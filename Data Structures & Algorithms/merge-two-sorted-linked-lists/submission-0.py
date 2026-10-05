# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = list1
        tail = list1
        if not list1:
            return list2

        if not list2:
            return list1
        if list1.val > list2.val:
            head = list2
            tail = list2
            list2 = list2.next
        else:
            list1 = list1.next
        while(list1 and list2):
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return head
        