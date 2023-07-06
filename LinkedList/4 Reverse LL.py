'''
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        next_node = None

        while current is not None:
            # Store the next node
            next_node = current.next
            # Reverse the pointer
            current.next = prev
            # Move the pointers one step forward
            prev = current
            current = next_node

        # After reversing, prev will be the new head of the reversed list
        return prev
