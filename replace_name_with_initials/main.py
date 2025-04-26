n = int(input())

names = []
for _ in range(n):
    names.append(input())

for name in sorted(names):
    parts = name.split()    
    print(f" {". ".join(map(lambda x: x[0], parts[:-1]))}. {parts[-1]}" )

   
#YAAAAAAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY! HUAAA HURRAYYY!!!!