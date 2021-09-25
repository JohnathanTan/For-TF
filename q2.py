def exists(var):
    """
    The function takes in a variable name in the form of a STR type.
    The function will check if the variable exists in the global scope.
    The function will not check the local scope as the logic resides within a function,
    hence the local scope will refer to variables within this function.
    
    
    Parameters
    ----------
    var : STRING
        The input is simply a string representation of the name of the variable in question.

    Returns
    -------
    bool
        Returns TRUE if the variable exists in the global scope, otherwise FALSE.

    """
    
    return var in globals()
    

print("Is variable 'a' defined globally?", exists("a"))

b = 1
print("Is variable 'b' defined globally?", exists("b"))   
