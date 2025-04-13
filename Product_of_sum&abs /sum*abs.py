def product_of_sum_and_abs_diff_of_digits(num: int):

    """Returns the product of the sum and absolute difference of digits of a two digit number.

    Assume number is a two digit number.

    Args:
        num (int) - The given number

    Returns:
        The required product.

    Examples:
        >>> product_of_sum_and_abs_diff_of_digits(38)
        55
        >>> product_of_sum_and_abs_diff_of_digits(55)
        0
    """
    a, b = map(int,str(num))        #[int(x) for x in str(num)]
    return (a + b) * abs(a - b)     # NOTE: x//10 gives floord division of 10 NOT ROUNDED OFF TO FLOOR DIVISION OF 10.....23//10 = 2 (NOT 20) 
num = int(input('Enter a two digit number: '))
print(product_of_sum_and_abs_diff_of_digits(num))


# MOST efficient way is using // and %  (MUCH FASTERRRRRR)  :

#  a, b = num // 10, num % 10
#     return (a + b) * abs(a - b)