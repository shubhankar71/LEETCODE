# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        m = []
        for i in range(len(lists)):
            current = lists[i]
            while current:
                m.append(current.val)
                current = current.next
        m.sort()
        dummy = ListNode(0)
        current = dummy

        for value in m:
            current.next = ListNode(value)
            current = current.next
        return dummy.next
        