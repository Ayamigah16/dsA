#QUESTION
"""
Write a function that accepts a string that contains all the letters of the
alphabet except one and returns the missing letter. For example, the string,
"the quick brown box jumps over a lazy dog" contains all the letters of the alphabet
except the letter, "f". The function should have a time complexity of O(N)
"""

def missingAlphabet(array):
    hashtable = {}
    for value in array:
        if value == " ":
            continue
        else:
            hashtable[value] = True
    
    alphabet = "abcdefghijklmnopqrstuvzxyz"
    for alpha in alphabet:
        if alpha not in hashtable.keys():
            return 
    
print(missingAlphabet("the quick brown box jumps over a lazy dog"))