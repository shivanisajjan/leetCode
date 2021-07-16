# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        sz = 0
        while curr != None:
            sz += 1
            curr = curr.next
        if sz == 1:
            return None
        elif sz == n:
            return head.next
        else:
            curr = head
            for i in range(sz - n - 1):
                curr = curr.next
            curr.next = curr.next.next
        return head



