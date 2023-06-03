# Question
"""Use recursion to write a function that accepts an array of strings and
returns the total number of characters across all the strings. For example,
if the input array is ["ab", "c", "def", "ghij"], the output should be 10 since there
are 10 characters in total"""


## using loop
def total_number_of_characters(array):
    sum = 0
    for string in array:
        sum = sum + len(string)
    return sum

## using recursion
def number_of_characters(array):
    if len(array) == 1:
        return len(array[0])
    
    return len(array[0]) + number_of_characters(array[1:])


print(number_of_characters(["ab", "c", "def", "ghij"]))