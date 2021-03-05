# What is a queue? 
 """
 a first-in-first-out (FIFO) data structure. In a FIFO data structure, the first element added to the queue will be the first one to be removed. This is equivalent to the requirement that once a new element is added, all elements that were added before have to be removed before the new element can be removed. A queue is an example of a linear data structure, or more abstractly a sequential collection.

FIFO operations
 queue.appendleft()
 queue.pop()

 """

# How does it work in memory?
"""
queue is implemented using the dynamic data structure Linked List. Using linked list for creating a queue makes it flexible in terms of size and storage. You don’t have to define the maximum number of elements in the queue.

Even in Java, queue is implimented using the linked list class

"""

# How is it implimented in python?
"""
we can use a list to impliemnt a queue but its not reccomeneded and its not FIFO friendly so we use pythons deque
"""
from collections import deque
q = deque()
q.appendleft(5)
q.pop()

#Impliment a queue class with deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)


# Big O analysis 
"""
Access:     O(n) 
Search:     O(n)  
Insertion:  O(1) 
Deletion:   o(1)
"""



#example application
