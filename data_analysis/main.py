def difference(data: list) -> list:
    """Returns a list of differences between consecutive elements in the input list.

    Args:
        data (list[float]): The list of numerical values.

    Returns:
        list[float]: A list of differences between consecutive elements.
    """
    
    
    return [data[i] - data[i-1] for i in range(1, len(data))]
    

def nth_order_difference(data: list, n: int) -> list:
    """Returns a list of nth order differences between consecutive elements in the input list.

    Args:
        data (list[float]): The list of numerical values.
        n (int): The order of the difference.

    Returns:
        list[float]: A list of nth order differences.
    """
    
    
    for i in range(n):
        data = difference(data)
    return data
    

def has_positive_trend(data: list) -> bool:
    """Returns True if the list has a positive trend, False otherwise.

    Args:
        data (list[float]): The list of numerical values.

    Returns:
        bool: True if the list has a positive trend, False otherwise.
    """
    
    
    return all(map(lambda x: x >= 0, difference(data)))
    

def moving_average(data: list, window_size: int) -> list:
    """Returns a list of moving averages of the input data with the given window size.

    Args:
        data (list[float]): The list of numerical values.
        window_size (int): The window size for the moving average.

    Returns:
        list[float]: A list of moving averages.
    """
    
    
    if len(data) < window_size:
        return []
    moving_averages = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        moving_averages.append(sum(window) / window_size)
    return moving_averages
    

def has_negative_average_trend(data: list, window_size: int) -> bool:
    """Returns True if the list has a negative trend after applying moving average with the given window size.

    Args:
        data (list): The list of numerical values.
        window_size (int): The window size for the moving average.

    Returns:
        bool: True if the average trend is negative, False otherwise.
    """
    
    
    return all(map(lambda x: x <= 0, difference(moving_average(data, window_size))))
    

