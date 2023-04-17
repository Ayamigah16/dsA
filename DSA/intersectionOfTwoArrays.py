# QUESTION
"""
Write a function that returns the intersection of two arrays. The intersection is a third array that contains all values contained within the first two
arrays. For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4].
Your function should have a complexity of O(N). (If your programming
language has a built-in way of doing this, don’t use it. The idea is to build
the algorithm yourself.)
"""

# ALGORITHM
"""
inputs => two given arrays( array1, array2)
outputs => intesction array(intesectionArray)

Target :: get compelexity of O(N)


"""


def intersectionSet(array1, array2):
    # determining the universal array based on size
    if len(array1) > len(array2):
        largerArray, smallerArray = array1, array2
    else:
        largerArray, smallerArray = array1, array2
    
    # using hashtables to store values of larger array
    hashTables = {}
    for value in largerArray:
        hashTables[value] = True
    
    # if values of smaller array is a key in larger array then part of intersection
    intersection = []
    
    for value in smallerArray:
        if value not in hashTables.keys():
            pass
        else:
            intersection.append(value)
    return intersection

# Test
array1 = [2, 4, 5, 6, 7, 13, 15, 43]
array2 = [5, 13, 20, 1, 7]

print(intersectionSet(array1, array2))
## worked