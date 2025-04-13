# call_log = [
#     {"name": "Alice", "duration": 300},
#     {"name": "Bob", "duration": 200},
#     {"name": "Alice", "duration": 100},
#     {"name": "Bob", "duration": 400},
#     {"name": "Charlie", "duration":300}
# ]


# get_call_count - {'Alice':2, 'Bob':2, 'Charlie': 1}
# get_total_call_duration - {'Alice': 400, 'Bob': 600, 'Charlie': 300}
# most_frequent_caller - 'Bob', (Alice and Bob has same number of calls but Bob has the most duration.)

def get_call_count(call_log):
    call_count = {}  
    for x in call_log:        # is same as " for x in  call_log.keys() "
        call_count[x['name']] = call_count.get(x['name'],0) + 1
    return call_count    


def get_total_call_duration(call_log):
    call_duration = {}
    for x in call_log:
        call_duration[x['name']] = call_duration.get(x['name'], 0) + x['duration']
    return call_duration

def  most_frequent_caller(call_log):
    call_count = get_call_count(call_log)
    call_duration = get_total_call_duration(call_log)
    return max(call_count, key = lambda x: (call_count[x],call_duration[x] ))

def process_call_log(call_log , task):
    if task == 'get_call_count':
        return get_call_count(call_log)
    elif task == 'get_total_call_duration':
        return get_total_call_duration(call_log)
    elif task == 'most_frequent_caller':
        return most_frequent_caller(call_log) 
    raise ValueError('Invalid task provided')

call_log = eval(input())
task = input()
print(process_call_log(call_log, task))










# def call_log_analysis(call_log):
