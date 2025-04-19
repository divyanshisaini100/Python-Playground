def are_orthogonal(t1: tuple, t2: tuple) -> bool:
    '''
    Check if two 2D vectors are orthogonal (perpendicular).

    Args:
        t1 (tuple): The first 2D vector (x, y).
        t2 (tuple): The second 2D vector (x, y).

    Returns:
        bool: True if the vectors are orthogonal, False otherwise.
    '''
    return (t1[0] * t2[0] + t1[1] * t2[1]) == 0

# dot product should be zero, for t1 & t2 to be orthogonal 
 