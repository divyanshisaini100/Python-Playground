
def absolute_time_difference(time1,time2):
    mins_time1 = total_mins(time1)
    mins_time2 = total_mins1(time2)
    diff = abs(mins_time1-mins_time2)    
    return (f"{diff//60:02}:{diff%60:02}")

def total_mins(t):
    return sum(x*60**i for i,x in enumerate(list(map(int,t.split(":"))))[::-1])   

def total_mins1(t):
    h,m = map(int, t.split(":"))    #map returns iterable objects, not list so can't use enumerate directly on map
    return h*60 + m
    

if __name__ =='__main__' : 
    time1 = input() 
    time2 = input()
    print(absolute_time_difference(time1,time2))
