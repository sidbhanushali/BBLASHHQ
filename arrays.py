# What is an Array? 
"""
a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key.
"""
my_array = ["stringz", 1, True, 4.2, None]

# How does it work in memory?
"""
DYNAMIC ARRAY IN PYTHON - will create additional memory locations on insertions and copys them

holds each data type sequencially in memory (RAM), to store the data on memory locations with addresses next to each other. Thats why in order to traverse, it will always be linear time best case.

Using the index, points to directly to the memory location of the target data value in the structure, making array access an o(1) runtime operation. 

https://miro.medium.com/max/497/1*-ImKrqrT14UlG6wMpAEIJQ.png

"""

# Big O analysis
"""
Access:     O(1) --> my_array[3]
Search:     O(n) --> for all in my_array: 
Insertion:  O(n) --> my_array.append(value)
Deletion:   o(n) --> my_array.pop() or my_array.remove(value)



Here is a link for all the built-in array/list methods in python: 
https://www.w3schools.com/python/python_ref_list.asp

"""


# How is it implimented in python?
"""
In python, arrays are implimented using the built-in "list" data structure

my_array = []
"""

#example application
"""
2 Sum leetcode (array / hashmap)
def two_sum(nums, target):
    my_hashmap = {}

    for i in range(len(nums)):
        curr = nums[i]
        if target - curr in my_hashmap:
            return (d[target - curr] + 1, i + 1)
        my_hashmap[curr] = i
    return None


"""