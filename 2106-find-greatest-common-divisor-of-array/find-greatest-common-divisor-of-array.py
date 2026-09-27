class Solution(object):
    def findGCD(self, nums):
        m=max(nums)
        n=min(nums)
        for i in range(1,n+1):
            if m%i==0 and n%i==0:

                ans=i
        return ans          
        
        