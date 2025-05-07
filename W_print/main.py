n = int(input())
for i in range(n):
    side_space = ' ' * (n - i - 1) # space between vertical bar | and / or \
    mid_space = ' '* 2 * i # middle space between / and \
    print(f"|{side_space}/{mid_space}\\{side_space}|")
