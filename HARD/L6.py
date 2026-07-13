
def isNumber(s):
    # if type(s) == float:
    #     if ord(s) in range(48,58):
    #         return True
    if len(s)>1:
        s = s[0]
        if ord(s) in range(48,58):
            return True
        else:
            return False
    if ord(s) in range(48,58):
        return True
    else:
        return False

n = "44"

print(isNumber(n))    
        
    
        