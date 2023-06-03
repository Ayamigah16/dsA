# QUESTION
"""
Use recursion to write a function that accepts a string and returns the
first index that contains the character “x.” For example, the string,
"abcdefghijklmnopqrstuvwxyz" has an “x” at index 23. To keep things simple,
assume the string definitely has at least one “x."
"""

# using loop
spam = "hahsamsa"
def index_of_X(string):
    if 'x' not in string:
        return -1
    
    for char in string:
        if char == "x":
            return string.index(char)

 

# using recursion
def x_index(string):
    # base case
    """
    if string has only one character ruturn 0; also string can't be empty
    """ 
    if string[0] == 'x':
        return 0
    
    return x_index(string[1:]) + 1
    
print(x_index('shjx'))