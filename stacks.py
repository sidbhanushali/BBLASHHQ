# What is a Stack? 
"""

 LIFO (last in, first out) like a stack of cards.

Abstract Stack Operations: 
- Stack.pop()
- Stack.push()
-Stack.peek()
-Stack.isEmpty()
-Stack.size()

"""

# How does it work in memory?
"""
any back button or "undo" feature will use a stack under the hood
"""

# How is it implimented in python?
"""
we can use the list data type in python to impliment stack (NOT RECCOMENDED)
- but the problem with a list is that its a dynamic array internally
"""
s = [] 
s.append('item 1')
s.pop('item 1') #removes and returns the element from the list
s[-1] #get the last element of
"""
OR 
we can use pythons deque from collections to impliment a stack
(RECOMNENDED) --> they are implimented using doubly linked lists so new memory is allocated when needed and no need to copy the new elements to the upgraded memory location like in an dynamic array
"""
from collections import deque

coolstack = deque()
coolstack.append("")

# implimenting a stack class using deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)


# Big O analysis 
"""
Access:     o(n) 
Search:     O(n)  
Insertion:  O(1) --> stack.push()
Deletion:   o(1) --> stack.pop()
"""

# example application
"""
https://www.youtube.com/watch?v=rrFkCswLYF0

Problem: Given A String with "<" denoting backspaces, output the final string
input: "hiy<frr<iend"
output: "hifriend"

"""
def backspace(inputstr):
    my_stack = []
    for char in inputstr:
        if char is not '<':
            my_stack.append(char)
        else:
            my_stack.pop()

    return ''.join(my_stack)