n = int(input())

names = []
for _ in range(n):
    names.append(input())

for name in sorted(names):
    parts = name.split()    
    print(f" {". ".join(map(lambda x: x[0], parts[:-1]))}. {parts[-1]}" ) 
    
# NOTICE even before printing parts[-1],  we gotta include ". " because join() functions works only in between (NOT AFTER END ONE, LIKE  WE WANT HERE) !!! 

   
#YAAAAAAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY! HUAAA HURRAYYY!!!!