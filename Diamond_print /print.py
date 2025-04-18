
m = int(input()) # 2n-1 lines
n = (m+1)//2
for i in range(1,n+1):
    print(" " * (n-i) + "*" * (2*i-1))
for i in range(n-1,0,-1):
    print(" " * (n-i) + "*" * (2*i-1))


# using f-string padding

for i in range(1, n+1):
    print(f'{"*" * (2*i - 1):^{m}}') 
for i in range(n-1,0,-1) :
    print(f'{"*" * (2*i - 1):^{m}}')  