# QUESTION
""" 
The following function uses recursion to calculate the Nth number from
a mathematical sequence known as the “Golomb sequence.” It’s terribly
inefficient, though! Use memoization to optimize it. (You don’t have to
actually understand how the Golomb sequence works to do this exercise.)

def golomb(n)
    return 1 if n == 1
    return 1 + golomb(n - golomb(golomb(n - 1)));
end
"""

# SOLUTION
""" 
def golomb(n, memo={}):
    return 1 if n == 1
    
    if !memo[n]:
        memo[n] = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)

    return memo[n]
"""