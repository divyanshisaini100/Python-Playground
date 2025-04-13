
def is_divisible_by_last_two_digits(num: int):
    a,b = (num%100)//10 , num%10        # just 'num//10' returns all values EXCEPT LAST DIGIT (think about it !!! )
    if a == 0 or b == 0:                # 0-case to be taken care of separately!
       return False
    elif num%a == 0 and num% b == 0 :
        return True
    return False

num = int(input())
print(is_divisible_by_last_two_digits(num))