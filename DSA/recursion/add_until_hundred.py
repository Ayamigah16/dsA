# QUESTION
"""
The following function accepts an array of numbers and returns the sum,
as long as a particular number doesn’t bring the sum above 100. If adding
a particular number will make the sum higher than 100, that number is
ignored. However, this function makes unnecessary recursive calls. Fix
the code to eliminate the unnecessary recursion:

def add_until_100(array)
    return 0 if array.length == 0
    if array[0] + add_until_100(array[1, array.length - 1]) > 100
        return add_until_100(array[1, array.length - 1])
    else
        return array[0] + add_until_100(array[1, array.length - 1])
    end
end
"""

# SOLUTION 
"""
def add_until_100(array)
    return 0 if array.length == 0

    sum_of_remaining_numbers = add_until_100(array[1, array.length - 1])

    if array[0] + sum_of_remaining_numbers > 100
        return sum_of_remaining_numbers
    else
        return array[0] + sum_of_remaining_numbers
    end
end
"""