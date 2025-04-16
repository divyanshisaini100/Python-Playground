n = int(input())

for i in range(1,n+1):
    zeros = " ".join("0"*i)
    print(" "*(n-i)+zeros)

# METHOD - 2 : using f-string padding

for i in range(1,n+1):
    zeroes = ' '.join('0'*i)
    print(f'{zeroes:^{2*n-1}}')     # NOTE: the use of brackets and how they work