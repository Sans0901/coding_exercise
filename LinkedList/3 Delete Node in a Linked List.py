237 Delete Node in a Linked List

'''
Example 1:


Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:


Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current = node
        previous = None
        
        while current.next is not None:
            current.val = current.next.val
            previous = current
            current = current.next
        
        # Reached the last node
        # Update the previous node's next pointer to None
        if previous is not None:
            previous.next = None
        else:
            # If the node to be deleted is the only node in the list
            node = None

# Optimized Solution

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
        vl = node.next.val
        node.val = vl
        node.next = node.next.next