class Solution(object):
    def isNumber(self, s):
        # if type(s) == float:
        #     if ord(s) in range(48,58):
        #         return True
        if len(s)>1 or len(s)<1:
            return False
        if ord(s) in range(48,58):
            return True
        else:
            return False
                
        
    
        