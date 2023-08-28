'''
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
             return NULL
        p = headA
        q = headB
        while (p != q):
            if (p is None):
                p =headB
            else:
                p = p.next
            if (q is None):
                q =headA
            else:
                q = q.next
        return p
        


Here we are transversing both the linkedlist till we found intersecting element while both starting points are not equal.

