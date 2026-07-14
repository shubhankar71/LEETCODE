import math
def isNumber(s):
    
    
    try:
        int(s)
        return True
    except ValueError:
        try:
            float(s)
            if math.isinf(float(s)) or math.isnan(float(s)):
                return False
            return True
        except ValueError:
            return False
                
        

n = "inf"


print(isNumber(n))    
        
    
        