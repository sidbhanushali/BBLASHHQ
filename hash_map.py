# What is a hash map? 
"""
an indexed data structure of key value pairs 
"""

# How does it work in memory?
"""
Implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

When you search through a hashmap / dict using a string index, it is o(1) time because under the hood, it is stored as an abstract array and uses a hashing function to convert the key into the "index" for the element in the hashmap_array that points to the memory location (my_dict['name'] --> Jon )


"""

# How is it implimented in python?

"""
We impliment it using pythons built in DICT data type
my_hashmap = {}

built-in dictionary methods in python 
https://www.w3schools.com/python/python_ref_dictionary.asp

"""

# Big O analysis 
"""
Access:     N/A 
Search:     O(1)  
Insertion:  O(1) 
Deletion:   o(1) 


*this is b/c hash map uses an abstract array to store the elements and runs the provided key thru a hashing function to point to the memory locations
"""

# example application
"""
leetcode 2 sum: 
does it in one pass and checks if target - curr is the compliment number
"""
def two_sum(nums, target):
    my_hashmap = {}

    for i in range(len(nums)):
        curr = nums[i]
        if target - curr in my_hashmap:
            return (my_hashmap[target - curr] + 1, i + 1)
        my_hashmap[curr] = i
    return None





# Collision handling in hash maps 
"""
https://www.geeksforgeeks.org/implementation-of-hashing-with-chaining-in-python/
"""