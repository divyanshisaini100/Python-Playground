
image = {"gif", "png", "jpeg" , "jpg" } 

with open( "data.txt", "r")  as f:
    info = f.read()

total_size = 0
for line in info.split():
    size, file = line.split(",")
    if file.lower().endswith(tuple(image)):
        total_size += int(size) 

print(total_size)
    