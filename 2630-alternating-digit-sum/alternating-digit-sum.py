class Solution(object):
    def alternateDigitSum(self, n):
        N=list(str(n))
        sum=0
       
        for i in range(len(N)):
            if i%2==0:
                sum+=int(N[i])
            else:
                sum-=int(N[i])
        return sum            


        

       

        
       
        
        