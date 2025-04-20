def has_no_vowels_in_even_indices(s: str) -> bool:
    """Checks if there are no vowels in even indices of a string.

    Args:
        s (str): The input string.

    Returns:
        bool: True if no vowels are in even indices, False otherwise.
    """
    even =  s[::2].lower() 
    for i in even:
        if i in 'aeiou':
            return False
    return True    

# PYTHONIC WAY
def has_no_vowels_in_even_indices1(s: str) -> bool:
    return not (set(s[::2].lower()) & set('aeiou'))  

# & is INTERSECTION - finds common elements----normally returns a set (empty if nothing common)
# But in Python, any object can be treated as True or False in a Boolean context (like inside an "if", or when using "not").
# empty set treated as FALSE
# NOT function negates the boolean value - True for False & vice-versa.