# implementing linear search for ordered array
def linear_search(array, value):
    for i in range(len(array) - 1):
        if array[i] == value:
            print("Value is at index : ", i)
            break
        elif array[i] > value:
            print("Value not found")
            break
               

#implementing binary search on ordered arrays
def binary_search(array, value):
    min = 0
    max = len(array) -1
    
    while(min <= max):
        mid = (min + max) // 2
        mid_value = array[mid]
        
        if mid_value == value:
            print("Value is at index : ", mid)
            break
        elif mid_value > value:
            max = mid - 1
        elif mid_value < value:
            min = mid + 1
            
    print("Value not found")

# implementing a bubble sort
def bubble_sort(list):
    unsorted_until_index = len(list) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i + 1]:
                list[i],list[i + 1] = list[i + 1], list[i]
                sorted = False 
        unsorted_until_index -= 1
    return list


# afunction to check for duplicate values
def hasDuplicateValue(array):
    steps = 0
    existingNumbers = list
    for i in range(len(array) - 1):
        steps += 1
        if existingNumbers[array[i]] == 1:
            return True
        else:
            existingNumbers[array[i]] = 1
    print(steps)
    return False 

 

"""
finds the greatest product of any pair of two numbers within a
given array
"""
def greatestProduct(array):
    greatestProductSoFar = array[0] * array[1]
    for i, ival in enumerate(array):
        for j, jval in enumerate(array):
            if i != j and ival * jval > greatestProductSoFar:
                greatestProductSoFar = ival * jval
    print(greatestProductSoFar)

 

"""def greatestNumber(array):
    for i in array:
        # Assume for now that i is the greatest:
        isIValTheGreatest = True
        
    for j in array:
        # If we find another value that is greater than i,
        # i is not the greatest:
        if j > i:
            isIValTheGreatest = False
            
        # If, by the time we checked all the other numbers, i
        # is still the greatest, it means that i is the greatest number:
        if isIValTheGreatest:
            return i"""        
def greatestNumber(array):
    greatestValue = array[0]
    
    for i in array:
        if i > greatestValue:
            greatestValue = i
    print(greatestValue)

def selctionSort(array):
    for i in range(len(array) - 1):
        lowestNumberIndex = i
        j = i + 1
        while(j != len(array)):
            if array[j] < array[lowestNumberIndex]:
                lowestNumberIndex = j
        
        if lowestNumberIndex != i:
            array[i], array[lowestNumberIndex] = array[lowestNumberIndex], array[i]
    print(array)


# implementation of insertion sort
def insertionSort(array):
    for index in range(1, len(array)):
        temp_value = array[index]
        position = index - 1
        
        while position >= 0:
            if array[position] > temp_value:
                array[position + 1] = array[position]
                position -= 1
            else:
                break
        array[position + 1] = temp_value
    return array

# finding the intersection of two sets
def intersection(firstArray, secondArray):
    result = []
    
    for i in range(len(firstArray) - 1):
        for j in range(len(secondArray) - 1):
            if firstArray[i] == secondArray[j]:
                result.append(firstArray[i])
                break
    print(result)


#  FINDING THE MEAN AVERAGE OF THE EVEN VALUES IN A LIST
def average_of_even_numbers(array):
    sum = 0
    count_of_even_numbers = 0
    for num in array:
        if num % 2 == 0:
            sum += num
            count_of_even_numbers += 1
    print(sum/count_of_even_numbers)


# a word builder function
def wordBuilder(array):
    collection = []
    for i in array:
        for j in array:
            if i != j:
                collection.append(i + j)
    return collection


# array sampling :: getting the first, mid and last values in an array
def sample(array):
    first = array[0]
    middle = array[int(len(array)/ 2)]
    last = array[-1]
    
    return ([first, middle, last])


def average_celsius(fahrenheit_readings):
    # collects celsius numbers
    celsius_numbers = []
    
    for fahrenheit_reading in fahrenheit_readings:
        celsius_conversion = (fahrenheit_reading - 32) / 1.8
        celsius_numbers.append(celsius_conversion)
        
    sum = 0
    for celsius_number in celsius_numbers:
        sum += celsius_number
    
    return sum / len(celsius_numbers)

# a function to print the sizes  of clothing items
def inventory(clothing_items):
    clothing_options = []
    for item in clothing_items:
        for size in range(1, 6):
            clothing_options.append(item + "Size: " + str(size))
    return clothing_options

# a function to count ones in an array
def count_ones(outer_array):
    count = 0
    for inner_array in outer_array:
        for number in inner_array:
            if number == 1:
                count += 1
    return count


def isPalindrome(string):
    min_index = 0
    max_index = len(string) - 1
    
    while min_index != max_index:
        if string[min_index] != string[max_index]:
            return False
        
        min_index += 1
        max_index -= 1
    return True

# haystack function
def find_needle(needle, haystack):
    needle_index = 0
    haystack_index = 0
    
    while haystack_index < len(haystack):
        if needle[needle_index] == haystack[haystack_index]:
            found_needle = True
            
            while needle_index < len(needle):
                if needle[needle_index] != haystack[haystack_index]:
                    found_needle = False
                    break
                needle_index += 1
            
            return found_needle
        haystack_index += 1
        
        # TODO: Complete the code
        


# array subset
def isSubset1(array1, array2):
    if len(array1) > len(array2):
        largerArray, smallerArray = array1, array2
    else:
        largerArray, smallerArray = array2, array1
    
    for i in range(len(smallerArray) - 1):
        foundMatch = False
        
        for j in range(len(largerArray) - 1):
            if smallerArray[i] == largerArray[j]:
                foundMatch = True
                break
        
        if foundMatch == False:
            return foundMatch
    return True

def isSubset2(array1,array2):
    if len(array1) > len(array2):
        largerArray, smallerArray = array1, array2
    else:
        largerArray, smallerArray = array2, array1
    
    hashTable = {}
    
    for value in largerArray:
        hashTable[value] = True
    
    for value in smallerArray:
        if not hashTable[value]:
            return False
    return True

# creating a stck class
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self,element):
        self.data.append(element)
        
    def pop(self):
        self.data.pop()
        
    def read(self):
        self.data[:-1]


class Linter:
    def __init__(self):
        # We use a simple array to serve as our stack:
        self.stack = Stack()
        
    def lint(self, text):
        # declaring inner functions
        def is_opening_brace(char):
            char in ["(", "[", "{"]
            
        def is_closing_brace(char):
            char in [")", "]", "}"]
        
        def is_not_a_match(opening_brace, closing_brace):
            match_brace = {"(":")", "[":"]", "{":"}"}            
              
            if (opening_brace, closing_brace) not in match_brace.items():
                return "Unmatched braces"
              
        # lint main       
        for char in text:
            # If the character is an opening brace:
            if is_opening_brace(char):
                # We push it onto the stack:
                self.stack.push()
                print("Buggy")
            # If the character is a closing brace:
            elif is_closing_brace(char):
                # Pop from stack:
                popped_opening_brace = self.stack.pop()
                
                # If the stack was empty, so what we popped was nil,
                # it means that an opening brace is missing:
                if popped_opening_brace == None:
                    return (char + "doesn't have opening braces")
                
                print("Buggy")
                # If the popped opening brace doesn't match the
                # current closing brace, we produce an error:
                is_not_a_match(popped_opening_brace, char)
                    
            # If we get to the end of line, and the stack isn't empty:
            if self.stack.read():
                return (self.stack.read() + "does not have closing braces")
            
        # Return true if line has no errors:
        return True
    
        
#linter = Linter()
#print(linter.lint("( var x = { y: [1, 2, 3]  )"))


# Recursion
# factorial_1.........(top - down approach)
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

# factorial_2 with extra parameters......(bottom - up approach)
def fact(number, i = 0, product = 1):
    if i > number:
        return product
    return fact(number, i + 1, product * i)

# countdown timer
def countdown(number):
    print(number)
    
    if (number == 0):
        return
    else:
        countdown(number - 1)

#countdown(7)

# doubling an array
## using a loop
def double_array(array):
    index = 0
    while (index < len(array)):
        array[index] *= 2
        index += 1
    return array
    
#print(double_array([2, 3, 5, 6, 8]))

## using recursion
def doubleArray(array, index = 0):
    # adding the base case
    if index >= len(array):
        return
    
    array[index] *= 2
    doubleArray(array, index + 1)
    return array

#print(doubleArray([3, 4, 6, 7]))

## array sum
def sumArray(array):
    # Base case: only one element in the array:
    if len(array) == 1:
        return array[0]
    
    return array[0] + sumArray(array[1:len(array)])

#print(sumArray([3,5,6]))

## STRING REVERSAL
def reverseString(string):
    # Base case: only one element in the array:
    if len(string) == 1:
        return string[0]   
    return reverseString(string[1:len(string)]) + string[0]

#print(reverseString("book"))

## count_x function ===> a function that counts the number of character "x" in a string
def count_x(string):
    '''if len(string) == 1:
        if string[0] == "x":
            return 1
        else:
            return 0'''
    # simplifying the above; an empty string will have no "x"
    if len(string) == 0:
        return 0
    
    if string[0] == "x":
        return 1 + count_x(string[1: len(string)])
    else:
        return count_x(string[1:len(string)])
        
#print(count_x("axbsxxxd"))


## the stair case problem
"""Let’s say we have a staircase of N steps, and a person has the ability to climb
one, two, or three steps at a time. How many different possible “paths” can
someone take to reach the top? Write a function that will calculate this for N
steps"""
def number_of_paths(n):
    # the base case
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
        
    return number_of_paths(n-1) + number_of_paths(n-2) + number_of_paths(n-3)

#print(number_of_paths(4))

## Anagram Generation
"""We’re going to write a function that returns an array of all anagrams of a
given string. An anagram is a reordering of all the characters within a string.
For example, the anagrams of "abc" are:
["abc",
"acb",
"bac",
"bca",
"cab",
"cba"]"""
def anagrams_of(string):
    # Base case: if the string is only one character,
    # return an array containing just a single-character string:
    if len(string) == 1:
        return string[0]
    
    # Create an array to hold all the anagrams:
    collection = []
    
    # Find all anagrams of the substring from the second character until
    # the end. For example, if the string is "abcd", the substring is "bcd",
    # so we'll find all anagrams of "bcd":
    substring_anagrams = anagrams_of(string[1:])
    
    # Iterate over each substring
    for substring_anagram in substring_anagrams:
        # Iterate over each index of the substring, from 0 until
        # one index past the end of the string:
        for index in range(len(substring_anagram) + 1):
            # Create a copy of the substring anagram:
            copy = substring_anagram[:]
            
            # Insert the first character of our string into the
            # substring anagram copy. Where it will go depends
            # on the index we're up to within this loop.
            # Then, take this new string and add it to our collection of anagrams:
            
            new_copy = copy[:index] + string[0] + copy[index:]
            collection.append(new_copy)
    return collection
print(anagrams_of("abc"))

