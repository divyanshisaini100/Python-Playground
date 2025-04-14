def swap_last_chars_of_values(d: dict, k1, k2):
    """Swap the last chars of the values of given keys in the dict.

    Args:
        d (dict): The dictionary with string values.
        k1: The first key.
        k2: The second key.

    Returns:
        None - modifies the dictionary in-place.
    """
    c1, c2 = d[k1][-1], d[k2][-1]
    d[k1] = d[k1][:-1]+c2
    d[k2] = d[k2][:-1]+c1
     
    # nOte: such no return function (def) can exist where changes happen IN-PLACE and  hence return NONE!