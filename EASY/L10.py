'''
Number of Elapsed Seconds Between Two Times

You are given two valid times startTime and endTime, each represented as a string in the format "HH:MM:SS".
Return the number of seconds that have elapsed from startTime to endTime.

 
Example 1:
Input: startTime = "01:00:00", endTime = "01:00:25"
Output: 25
Explanation:
endTime is 25 seconds ahead of startTime.

Example 2:
Input: startTime = "12:34:56", endTime = "13:00:00"
Output: 1504
Explanation:
endTime is 25 minutes and 4 seconds ahead of startTime, which equals 1504 seconds
'''

def secondsBetweenTimes( startTime, endTime):
    h1 = int(startTime[0:2])
    m1= int(startTime[3:5])
    s1= int(startTime[6:8])
    h2 = int(endTime[0:2])
    m2= int(endTime[3:5])
    s2= int(endTime[6:8])
    
    h1 = (h1 * 60 * 60)
    m1 = (m1 *60)
    h2 = (h2 *60*60)
    m2 = (m2*60)

    T1 = h1+m1+s1
    T2= h2+m2+s2
    
    return T2-T1
    
n= "12:34:56"
m= "13:00:00"

print(secondsBetweenTimes(n,m))
