# https://leetcode.com/problems/reverse-linked-list/solution/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while (head != None):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


# https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next


# https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hashset = set()
        while headA != None:
            hashset.add(headA)
            headA = headA.next
        while headB != None:
            if headB in hashset:
                return headB
            headB = headB.next
        return None