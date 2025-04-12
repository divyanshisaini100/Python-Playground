def number_with_more_unique_digits(n1:int, n2:int):
    """
    Compares two integers and returns the one with more unique digits.

    Args:
        n1 (int): The first integer.
        n2 (int): The second integer.

    Returns:
        int or tuple: The integer with more unique digits. 
        If both numbers have the same number of unique digits, 
        returns a tuple of both integers `(n1, n2)`.

    Example:
        >>> number_with_more_unique_digits(123, 1122)
        123

        >>> number_with_more_unique_digits(1122, 2211)
        (1122, 2211)
    """
    s1 = set(map(int, str(abs(n1))))       # equivalent to 'set(int(x) for x in str(abs(n1)))' 
    s2 = set(int(x) for x in str(abs(n2))) # set(str(abs(n1))) also works here BUT returns each element in set as 'str' not 'int' (BUT WE DON'T NEED IT TO BE 'int' HERE)  
    
                                           # len_n1 = len(set(str(abs(n1))))  ....TO DO IT DIRECTLY!!
        
    if len(s1)>len(s2):
        return n1
    elif len(s1)<len(s2):
        return n2
    else:
        return (n1,n2)
