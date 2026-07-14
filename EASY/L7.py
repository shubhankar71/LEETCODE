def areNumbersAscending( s):
    s = s.split()
    ss =[]
    for word in s:
        if word.isdigit():
            ss.append(int(word))
    print(ss)
    i = 0
    while i!= len(ss)-1:
        if ss[i]<ss[i+1]:
            i = i+1
            
        elif ss[i+1]==ss[i]:
            i = i+1
            return False
        else:
            return False
    return True    

                
    

s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
print(areNumbersAscending(s))
