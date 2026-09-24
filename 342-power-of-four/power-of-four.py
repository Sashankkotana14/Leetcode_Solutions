class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        i=0
        while 4**i<=n:
            if 4**i==n:
                return True
            i+=1 
        return False            
        
        