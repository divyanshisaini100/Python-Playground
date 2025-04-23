n = int(input())
for i in range(n):
   s = input().lower()
   for char in s:
      if char in 'aeiou':
         char = char.upper()
      print (char,end ="")

for i in range(n):
    line = input()
    print("".join([c.upper() if c.lower() in "aeiou" else c.lower() for c in line]))

