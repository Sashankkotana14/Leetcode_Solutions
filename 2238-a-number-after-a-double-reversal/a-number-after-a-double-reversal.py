class Solution(object):
    def isSameAfterReversals(self, num):
        reverse_1=int(str(num)[::-1])
        reverse_2=int(str(reverse_1)[::-1])
        if num==reverse_2:
            return True
        else:
            return False    
        
        
        