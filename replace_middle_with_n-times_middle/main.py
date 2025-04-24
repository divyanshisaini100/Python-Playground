def replace_middle_with_n_times_middle(t: tuple, n: int) -> tuple:
    '''
    Replace the middle element of a tuple with `n` copies of the middle element.

    Args:
        t (tuple): A tuple with an odd number of elements.
        n (int): The number of times the middle element should be repeated.

    Returns:
        tuple: A new tuple with the middle element replaced by `n` copies.
    '''
    l = len(t)//2 
    return t[:l]+', '.join(t[l]*n)+t[l+1:]                # "".join().... here is 'STRING WITH SEPARATOR'



#BELOW IS ACCURATE AND CORRECT  CODE! (RESULTS IN TUPLE ONLY! ....NOT THE ABOVE ONE!....NOTE THE MISTAKE!)
 
def replace_middle_with_n_times_middle1(t: tuple, n: int) -> tuple:
    m = len(t) // 2
    return t[:m] + (t[m],) * n + t[m + 1:]               # here (t[m],) is 'TUPLE WITH REPEATED ELEMENTS'    NOTE: MORE ACCURATE GIVEN A TUPLE !!! (ABOVE ONE DOESNT' GIVE TUPLE BUT STRING IN TUPLE KINDA...IT'S MIXXX!)



t = tuple(input())
n = int(input())
print(replace_middle_with_n_times_middle1(t,n))



#NOTE:
#        (x,) creates a 1-element tuple — great for tuple manipulation.
#        + can only combine same types: string+string or tuple+tuple.

# If the user inputs: 
# 12345
# Then:
# t = tuple(input())  # becomes ('1', '2', '3', '4', '5')

# Ask for input like this:
#     1 2 12 3 56
# And convert it properly:
#     t = tuple(map(int, input().split()))
# This gives you:
#     (1, 2, 12, 3, 56)   