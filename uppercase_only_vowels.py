n = int(input())
for i in range(n):
   s = input().lower()
   for char in s:
      if char in 'aeiou':
         char = char.upper()
      print (char,end ="")
   print()   #to move to next line after every line 

#NOTE: Below is more efficient code :-     

# for i in range(n):
#     line = input()
#     print("".join([c.upper() if c.lower() in "aeiou" else c.lower() for c in line]))

