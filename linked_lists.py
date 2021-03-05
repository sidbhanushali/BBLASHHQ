# What is a Linked List? 
"""
 a linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next.
 
  It is a data structure consisting of a collection of nodes which together represent a sequence.
    each node contains: data, and a pointer to the next node in the sequence. 
    The last node points to null

"""

# How does it work in memory?
 """
 random memory locations with pointers to the next node in the sequence
 https://miro.medium.com/max/1468/1*sBUu3B4LnXxmKV1P5FVbWg.png
 """

# Big O analysis 
"""
Access:     O(n) 
Search:     O(n)  
Insertion:  O(1) 
Deletion:   o(1)
"""


# How is it implimented in python?
"""
Linked list class
"""

class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


# example application
"""
reverse a linked list
https://leetcode.com/problems/reverse-linked-list/#/description
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev 
            prev = temp

