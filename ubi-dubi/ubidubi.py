with open("paragraph.txt", 'r' ) as f:
    
    text = f.read()
    
    vowel_count = 0
    for line in text:
        for char in line:
            if char.lowercase() in 'aeiou':
                if vowel_count/2 == 0:
                    print('ubi',end='') 
                else:
                    print('dubi',end='')
                vowel_count+=1    
            print(char, end='')
