#QUESTION
"""
Write a function that accepts an array of strings and returns the first
duplicate value it finds. For example, if the array is ["a", "b", "c", "d", "c", "e",
"f"], the function should return "c", since it’s duplicated within the array.
(You can assume that there’s one pair of duplicates within the array.)
Make sure the function has an efficiency of O(N).
"""

#ALGORITHM
"""
inputs ==> single array( array )
output ==> first string duplicate

"""
# with complexity O(N^2)
def stringDuplicate(array):
    i = 1   # defining a counter for inner loop
    for element in  range(len(array) - 1):
        
        for value in range(i, len(array) - 1):
            if array[element] == array[value]:
                return array[element]
        i += 1
    return ("No duplicate")
            
def mainStringDuplicate(array):
    # storing array
    hashtable = {}
    count = 1
    for value in array:
        if value in hashtable.keys():
            return value
        hashtable[value] = 1
        
         

print(mainStringDuplicate(["a","b","c","d","c","e"]))
    
    
#print(stringDuplicate(["a","b","c","d","c","e"]))