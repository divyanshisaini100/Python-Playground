# data = {
#     "Alice": [90, 80, 85],
#     "Bob": [40, 50, 60],
#     "Charlie": [30, 40, 20], 
#     "Ram": [78, 92, 85, 79, 81],
#     "Babu": [67, 70, 75],
#     "Kumar": [ 100, 100, 100, 100, 100, 100, 40]
# }
# print(filter_students(data, 'excellent')) # Output: {'Alice', 'Kumar'}
# print(filter_students(data, 'good')) # Output: {'Babu', 'Bob', 'Ram'}
# print(filter_students(data, 'all_pass')) # Output: {'Alice', 'Babu', 'Ram'}
# print(filter_students(data, 'balanced')) # Output: {'Alice', 'Babu'}

    

def avg(lst):
    if not lst:             #tho not req in this case but a good practise still
        return 0               # or "float(nan)" ... to indicate 'undefined' or 'Not A Number'
    return sum(lst)/len(lst)

def excellent(data):
    s = set()
    for key,value in data.items():
        if avg(value) >= 85 :
            s.add(key)
    return s        

def good(data):
    s = set()
    for key,value in data.items():
        if 50 <= avg(value) < 85 :
            s.add(key)         
    return s 

def all_pass(data):
    s = set()
    for key,value in data.items():                       
        if all(i>=50 for i in value):
            s.add(key)
    return s       
    
# without using 'all' func

def all_pass1(data):
    s = set()
    for key,value in data.items():
        passed = True
        for i in value:
            if i<50:
                passed = False
                break
        if passed:
            s.add(key)
    return s

def balanced(data):
    s = set()       
    for key,value in data.items():
        if max(value) - min(value) <=10:
            s.add(key)
    return s    

def filter_students(data: dict, filter: str) -> set:
    '''
    Takes a dictionary where keys are student names and values are lists of scores, filters names based on the given criteria
     - "excellent" - average score >= 85.
     - "good" - average score >= 50 and < 85.
     - "all_pass" - all scores >= 50.
     - "balanced" - difference between min and max is <= 10.
   
    Args:
        scores(dict)  : keys are student names and values are lists of scores

    Returns:
        set: Set of roll numbers matching the criteria
    '''
    if filter == 'balanced':
        return balanced(data) 
    if filter == 'all_pass':
        return all_pass(data) and all_pass1(data)
    if filter == 'good':
        return good(data)
    if filter == 'excellent':
        return excellent(data)

data = eval(input())  
print (filter_students(data,'good'))  #var needs to be within ' ' quotes
print (filter_students(data,'all_pass'))
print (filter_students(data,'excellent'))
print (filter_students(data,'balanced'))