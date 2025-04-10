n = int(input('Enter a positive integer: '))

while n<=0:
       n = int(input('Enter a POSITIVE integer: '))

print("\nRight Slanting")         
for i in range(1,n+1):
        print('*'*i)
     
print("\nLeft Slanting")
for i in range(1,n+1):
        print(" "*(n-i)+ "*"*i)
        
