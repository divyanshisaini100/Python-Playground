with open("paragraph.txt", 'r' ) as f:     
      
     #'r' is default
    # text = f.read() ....makes it into a single long string and then you directly go 'for char in text: '
    # for line in f ....reads it line by line and then you need 'for char in line: '
      
    vowel_count = 0
    for line in f:
        for char in line:
            if char.lower() in 'aeiou':
                if vowel_count % 2 == 0:
                    print('ub',end='') 
                else:
                    print('dub',end='')
                vowel_count+=1    
            print(char, end='')


# hubelldubo wuborld
# pythdubon ubis gduboubod            
