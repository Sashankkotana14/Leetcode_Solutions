class Solution(object):
    def plusOne(self, digits):
        num=0
        for i in digits:
            num=(num*10)+i
            a=num+1
        return list(map(int,str(a)))
        
        