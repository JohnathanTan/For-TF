def pascal_triangle_multiplicative(n):
    """
    A pascal triangle can be computed by from a series of binomial expansions in the form of (a + b)^n.
    Where n increments by 1 from 0 to infinity.
    The numbers in the n-th row of the pascal triangle will refer to the the coefficients of the expanded binomial expression.
    This function implements the multiplicative method of computing the coefficients which is faster than the factorial method. 
    
    
    Parameters
    ----------
    n : INT
        Refers to the n-th row of a pascal triangle.

    Returns
    -------
    list
        Returns a list of numbers that exists in the nth row of a pascal triangle.

    """
    
    previous_term = 1
    term = previous_term
    arr = [term] # initial/boundary value
    
    for r in range(1, n+1):
        term *= (n + 1 - r) / r
        arr.append(int(term))
        previous_term = term

    return arr


# Set n value
n = 5

# To print at n-th row
print("For a single row given n={}:".format(n))
print(pascal_triangle_multiplicative(n), end="\n\n")

# Print from 0 to n-th
print("For a complete pascal triangle given n={}:".format(n))
for i in range(n + 1):
    print(pascal_triangle_multiplicative(i))
    
    


