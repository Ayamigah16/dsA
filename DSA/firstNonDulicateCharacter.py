# QUESTION
"""
Write a function that returns the first non-duplicated character in a string.
For example, the string, "minimum" has two characters that only exist
once—the "n" and the "u", so your function should return the "n", since it
occurs first. The function should have an efficiency of O(N).
"""
def firstNonDuplicateCharacter(string):
    hashtable = {}
    count = 1
    for value in string:
        if value not in hashtable.keys():
            hashtable[value] = 1
        else:
            hashtable[value] = (hashtable[value] + 1)
    
    for value in hashtable.keys():
        if hashtable[value] == 1:
            return value
        
print(firstNonDuplicateCharacter("minimum"))