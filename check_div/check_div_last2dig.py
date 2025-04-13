
def is_divisible_by_last_two_digits(num: int):
    a,b = (num%100)//10 , num%10        # just 'num//10' returns all values EXCEPT LAST DIGIT (think about it !!! )
    if a == 0 or b == 0:                # 0-case to be taken care of separately!
       return False
    elif num%a == 0 and num% b == 0 :
        return True
    return False


num = int(input())
print(is_divisible_by_last_two_digits(num))

# MORE EFFICIENT CODE:
def is_divisible_by_last_two_digits1(num):
        
        a,b = str(num)[-2:]                      #NOTE: how string index is directly converted to var(s)
        a, b = int(a), int(b)                    # But say a,b = str(num)[-3,]... then python raise an error "TOO MANY VALUES TO UNPACK"....but if var = str indices then python automatically UNPACKS AND ASSIGNS VALUES 
        return a!=0 and b!=0 and num % a == 0 and num % b == 0

def is_divisible_by_last_two_digits2(num):
     a,b = map(int, str(num)[-2:])
     return a!=0 and b!=0 and num%a == 0 and num%b == 0