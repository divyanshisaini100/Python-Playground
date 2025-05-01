# Time Series Analysis
Given a list of numerical values, implement the following functions to analyze its trend:

**difference(data: list)** -> list: Returns a list of differences between consecutive elements in the input list.
**nth_order_difference(data: list, n: int)** -> list: Returns a list of nth order differences between consecutive elements in the input list.
**has_positive_trend(data: list)** -> bool: Returns True if the list has a positive trend, False otherwise.
**moving_average(data: list, window_size: int)** -> list: Returns a list of moving averages of the input data with the given window size.
**has_negative_average_trend(data: list, window_size: int)** -> bool: Returns True if the list has a negative trend after applying a moving average with the given window size.


***Example***

data1 = [1, 3, 5, 7, 9]
data2 = [10, 8, 6, 4, 2]
data3 = [1, 2, 1, 0, -1]

print(has_positive_trend(data1))  # True