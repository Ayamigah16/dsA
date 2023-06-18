# QUESTION
"""Use recursion to write a function that accepts an array of numbers and
returns a new array containing just the even numbers."""

# SOLUTION
""" 
sample_input = [2, 4, 5, 6, 8, 11]
sample_output = [2, 8, 6, 8]
"""
## Using a loop
def filter_even(array):
    output = []
    index = 0
    while (index < len(array)):
        if array[index] % 2 == 0:
            output.append(array[index])
        index += 1
    return output

print(filter_even([2, 4, 5, 6, 8, 11]))

def filterEven(array):
    print("Even")
    if len(array) < 1:
        return
    
    if array[0] % 2 == 0:
        return [array[0]] + [filterEven(array[1:])]
    else:
        return filterEven(array[1:])
    #return filterEven(array[1:len(array)])
    

spam = [1,2,4] + [5, 6, 7]
print(filterEven(spam))